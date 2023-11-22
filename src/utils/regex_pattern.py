""" Module that contains logic for comparing the regex patterns for particular input validation."""
import logging
import re

from src.config.prompts import PromptsConfig
from src.logs.log_config import LogConfig

logger = logging.getLogger('regex_pattern')

BOOKING_ID_REGEX = r"^BOOK[a-zA-Z0-9]+$"
EMAIL_REGEX = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
MOBILE_NO_REGEX = r"[6-9][0-9]{9}$"
NAME_REGEX = r"^([A-Za-z]{2,25}\s*)"
PARKING_SLOT_NUMBER_REGEX = r"^PSN[0-9]+$"
PASSWORD_PATTERN = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"
ROLE_REGEX = r"^([a-z]){5,}$"
STRING_REGEX = r"^[a-zA-Z]+\s*"
TYPE_ID_REGEX = r"^TYPE[a-zA-Z0-9]+$"
USERNAME_REGEX = r"(^user@)([a-z]{5,})"
VEHICLE_NUMBER_REGEX =r"^[A-Z]{2}[-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}$"

def error_handling_input(func):
    """Decorator for input validation and error handling during customer registration."""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is False or result is None:
                raise Exception
        except Exception:
            logger.debug(LogConfig.INVALID_INPUT_EXCEPTION_INFO)
            print(PromptsConfig.INVALID_INPUT+ "\n")
        finally:
            return result
    return wrapper

@error_handling_input
def input_validation(regular_exp: str, input_field: str) -> bool:
    """Function to validate input on basis of regex."""
    result = re.match(regular_exp, input_field) 
    if result is not None:
        return True
    else:
        return False
        