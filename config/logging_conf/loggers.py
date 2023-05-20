import logging

from config.logging_conf.handlers import MultiLineHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(MultiLineHandler(line_length=80))
