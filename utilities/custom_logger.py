import logging
class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\guru99.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger