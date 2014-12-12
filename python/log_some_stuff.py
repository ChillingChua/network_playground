# just some minimal logging instances to
# test the funtionality of the check_mk puppet
# module timing log parser

import atexit
from multiprocessing import Process
from writer import LogWriter

all_writers = []

@atexit.register
def stop():
    for obj in all_writers:
        obj.stop()


def getWriter(log_file, base_string):
    l = LogWriter(log_file, base_string)
    l.start()
    all_writers.append(l)

a = Process(target=getWriter, args=('/tmp/logfile1.log', '%s - [%s] some process took %s seconds.'))
b = Process(target=getWriter, args=('/tmp/logfile2.log', '%s - [%s] %s -> thats too long !!'))
a.start()
b.start()
b.join()
