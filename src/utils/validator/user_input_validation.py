"""Module for validating user related inputs."""
import re
import logging 

from config.prompts import PromptsConfig
from logs.log_config import LogConfig
import utils.regex_pattern as Regex

logger = logging.getLogger('validations')

class UserInputValidation:
    """This class contains methods for validating user realted input."""
    @staticmethod
    def input_name() -> str:
        """Validation of name using regular expression."""
        while True:
            name = input(PromptsConfig.INPUT_NAME).strip()
            is_valid_name = Regex.input_validation(Regex.NAME_REGEX, name)
            if is_valid_name:
                return name.title()

    @staticmethod
    def input_username() -> str:
        """Validation for username using regular expression."""
        while True:
            print(PromptsConfig.USERNAME_FORMAT)
            username = input(PromptsConfig.INPUT_USERNAME).strip()
            is_valid_username = Regex.input_validation(Regex.USERNAME_REGEX, username)
            if is_valid_username:
                return username.lower()
           
    @staticmethod
    def input_age() -> int:
        """Validation of age."""
        while True:
            try:
                age = int(input(PromptsConfig.INPUT_EMPLOYEE_AGE))
                if age > 60 or age < 15:
                    print(PromptsConfig.AGE_RESTRICTION + "\n")
                    continue
                return age
            except TypeError as error:
                logger.debug(error)
                print(PromptsConfig.NUMBER_INPUT.format("Age") + "\n")

    @staticmethod
    def input_gender() -> str:
        """Validation of gender."""
        while True:
            try:
                gender = input(PromptsConfig.INPUT_EMPLOYEE_GENDER).strip().capitalize()
                if gender == "F":
                    return "Female"
                elif gender == "M":
                    return "Male"
                else:
                    raise ValueError
            except ValueError as e:
                logger.debug(e)
                print(PromptsConfig.INVALID_INPUT)
   
    @staticmethod
    def input_role() -> str:
        """ Validation of role using regular expression."""
        while True:
            role = input(PromptsConfig.INPUT_EMPLOYEE_ROLE).strip().lower()
            is_valid_role = Regex.input_validation(Regex.ROLE_REGEX, role)
            if role == "admin":
                print(PromptsConfig.CANNOT_CREATE_ADMIN + "\n")
                continue
            if is_valid_role:
                return role
            
    @staticmethod
    def input_email_address() -> str:
        """Validation of email address using regular expression."""
        while True:
            email = input(PromptsConfig.INPUT_EMPLOYEE_EMAIL).strip()
            is_valid_email = Regex.input_validation(Regex.EMAIL_REGEX, email)
            if is_valid_email:
                return email.lower()

    @staticmethod
    def input_mobile_number() -> str:
        """Validation of phone number using regular expression."""
        while True:
            mobile_number = input(PromptsConfig.INPUT_MOBILE_NUMBER).strip()
            is_valid_mobile_number = Regex.input_validation(Regex.MOBILE_NO_REGEX, mobile_number)
            if is_valid_mobile_number:
                return mobile_number
