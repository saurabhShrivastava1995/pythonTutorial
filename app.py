import logging
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",level=logging.DEBUG)
logger = logging.getLogger("testlogger")
logger.warning("This is warning")
logger.debug("This is debug")

