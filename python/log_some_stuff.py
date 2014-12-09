# just some minimal logging instances to
# test the funtionality of the check_mk puppet
# module timing log parser

import atexit
from lib.writer import LogWriter

all_writers = []

@atexit.register
def stop():
    for obj in all_writers:
        obj.stop()

log_writer_1 = LogWriter('logs/logfile1.log', 'some process took %s seconds.')
log_writer_1.start()
all_writers.append(log_writer_1)

log_writer_2 = LogWriter('logs/logfile2.log', '%s -> thats too long !!')
log_writer_2.start()
all_writers.append(log_writer_2)
