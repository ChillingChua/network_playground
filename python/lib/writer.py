import logging
import random
import time


class LogWriter:

    def __init__(self, filename, base_string):

        logging.basicConfig(filename=filename, level=logging.DEBUG)

        self.log = logging.getLogger('LogWriter')
        random.seed(time.time())
        self.filename = filename
        self.base_string = base_string
        self.run = True

    def start(self):
        self.log.info('Starting ...')
        while self.run:
            duration = random.randint(0,15) + random.random()
            time.sleep(duration)
            self.log.info(self.base_string % str(duration))

    def stop(self):
        self.log.info('Stopping ...')
        self.run = False
