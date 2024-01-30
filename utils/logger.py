import logging
import inspect

class Logger:
    def __init__(self, log_level=logging.DEBUG):
        # Set class/method name from where it's called
        logger_name = inspect.stack()[1][3]
        # create logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        # Check if the logger already has a handler
        if not self.logger.handlers:
            # create file handler and set the log level
            fh = logging.FileHandler("automation.log")
            # create formatter - how you want your logs to be formatted
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s : %(message)s",
                datefmt="%d.%m.%Y %H:%M:%S",
            )
            # add formatter to file handler
            fh.setFormatter(formatter)
            # add file handler to logger (only if no handler exists)
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger