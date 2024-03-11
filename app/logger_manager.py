
import os
import sys
from os.path import join
import logging
from logging import getLogger, DEBUG, StreamHandler, FileHandler, Formatter

from utils import get_current_datetime_str


def get_logger(name, level=DEBUG):
  """Create logger for console & file.

  Args:
      name (str): module name. should be __name__.
      level (int, optional): stream handler level. Defaults to DEBUG.

  Returns:
      Logger: logger.

  """
  logger = getLogger(name)
  logger.setLevel(DEBUG)  # root level (Handler level is overrieded if it is lower than root level)

  # StreamHandler
  handler = StreamHandler()
  handler.setLevel(level)
  handler.setFormatter(Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
  logger.addHandler(handler)

  # FileHandler
  _detail_formatting = \
    "%(asctime)s - %(name)s - %(levelname)s - %(processName)-10s - %(threadName)s - %(message)s"
  _arg_str = os.path.splitext(sys.argv[0])[0]  # created by nishizawa senpai
  _arg_str = _arg_str.split('/')[-1]
  _file_name = get_current_datetime_str() + '_' + str(_arg_str) + '.log'
  handler = FileHandler(filename=join(os.getcwd(), "log", _file_name))
  handler.setFormatter(Formatter(_detail_formatting))
  logger.addHandler(handler)

  # logger.propagate = False

  return logger