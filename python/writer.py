import hashlib
import logging
import random
import time

from CassandraLogHandler import CassandraLogHandler
from mx import DateTime

HOST = '127.0.0.1'
KEYSPACE = 'log_test'


class LogWriter:

    def __init__(self, filename, base_string):

        logging.basicConfig(filename=filename, level=logging.DEBUG)
        self.log = logging.getLogger('LogWriter')
        cassandra_handler = CassandraLogHandler(HOST, KEYSPACE)
        self.log.addHandler(cassandra_handler)

        random.seed(time.time())
        self.filename = filename
        self.base_string = base_string
        self.run = True

    def start(self):
        self.log.info('Starting ...')
        while self.run:
            idx = str(hashlib.md5(str(random.random())).hexdigest())
            date_string = DateTime.now().strftime('%Y/%m/%d %H:%M:%S')
            duration = random.randint(0, 15) + random.random()
            time.sleep(duration)
            self.log.debug(self.base_string % (date_string, idx, str(duration)))

    def stop(self):
        self.log.info('Stopping ...')
        self.run = False
