from logging import INFO
from logger_manager import get_logger

logger = get_logger(__name__, INFO)


str = "Hello World."
print(str)
logger.info(str)