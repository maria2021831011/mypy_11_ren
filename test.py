from mypy_11_ren.logger import logger 
from mypy_11_ren.custom_exception import InvalidURLException

# logger.info("This is a test log message from test.py")

try: 
    raise InvalidURLException()
except Exception as e:
    logger.error(f"Caught an exception: {e}")