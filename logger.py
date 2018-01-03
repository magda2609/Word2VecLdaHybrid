import settings as settings
import logging


class Logger:

    def __init__(self):
        self.log_file = settings.LOG_FILE
        self.log_level = settings.LOG_LEVEL

    def get_logger(self, name):
        logger = logging.getLogger(name)

        logger.setLevel(self.log_level)

        fh = logging.FileHandler(self.log_file)
        fh.setLevel(self.log_level)

        ch = logging.StreamHandler()
        ch.setLevel(self.log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger
