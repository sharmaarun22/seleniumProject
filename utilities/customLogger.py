import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        try:
            log_directory = ".\\Logs\\"
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)
            logging.basicConfig(filename=log_directory + "automation.log",
                                format='%(asctime)s:%(levelname)s:%(message)s',
                                datefmt='%d%m%Y %I%M%S %p')
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            return logger
        except Exception as e:
            print(f"Error setting up logging: {e}")


