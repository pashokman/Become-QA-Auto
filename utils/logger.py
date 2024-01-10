import logging
import inspect


class Logger():
    
    def custom_logger(log_level=logging.DEBUG):
        # Set calss/method name from where its called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        # create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s : %(message)s",
            datefmt="%d.%m.%Y %H:%M:%S",
        )
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)
        return logger