__author__ = 'awerner'

import logging
import re
import traceback
import uuid

from cassandra.cluster import Cluster
from mx import DateTime


class CassandraLogHandler(logging.Handler):

    def __init__(self, cluster, keyspace):
        logging.Handler.__init__(self)
        self.cluster = cluster
        self.keyspace = keyspace
        self.connection = self._getConnection()
        self.regex = re.compile('^(?P<log_date>\d{4}\/\d{2}\/\d{2}\s\d{2}:\d{2}:\d{2})\s\-\s(?P<session_id>\[\w+\])?(?P<message>.*)')
        self.insert_stmt = "INSERT INTO log (id, session_id, log_date, log_level, message) VALUES ('%s', '%s', %s, '%s', '%s')"

    def _getConnection(self):
        if not isinstance(self.cluster, list):
            self.cluster = [self.cluster, ]
        c = Cluster(self.cluster)
        try:
            session = c.connect()
            session.set_keyspace(self.keyspace)
            return session
        except Exception:
            print 'Could not establish cassandra session for cluster: %s -> %s' % (str(self.cluster),
                                                                                   str(self.keyspace))

    def _parseRecord(self, record):
        return re.match(self.regex, record.msg)

    def emit(self, record):
        try:
            data = self._parseRecord(record)
            idx = uuid.uuid1()
            if data:
                now = int(DateTime.DateTimeFrom(data.group('log_date')))
                self.connection.execute(self.insert_stmt % (idx, data.group('session_id')[1:-1], now,
                                                            record.levelname, data.group('message').strip()))
            else:
                now = int(DateTime.now().ticks())
                self.connection.execute(self.insert_stmt % (idx, 'no_session_id', now,
                                                            record.levelname, record.msg.strip()))
        except:
            print 'Emit failed !'
            print traceback.print_exc()
            print 'cluster: %s' % str(self.cluster)
            print 'keyspace: %s' % str(self.keyspace)
            print 'record: %s' % str(record)
