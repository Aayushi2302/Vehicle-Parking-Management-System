"""Module for validating parking management related inputs."""
from datetime import datetime
import logging
import re

from config.prompts import PromptsConfig
from logs.log_config import LogConfig
import utils.regex_pattern as Regex

logger = logging.getLogger('validations')
    
class ParkingManagerInputValidation:
    """This class contains methods for validating parking management related inputs."""
    @staticmethod
    def input_vehicle_type_name() -> str:
        """Validation of vehicle_type name using regular expression."""
        while True:
            type_name = input(PromptsConfig.INPUT_TYPE_NAME).strip()
            is_valid_type_name = Regex.input_validation(Regex.STRING_REGEX, type_name)
            if is_valid_type_name:
                return type_name.title()

    @staticmethod
    def input_price_per_hour() -> float:
        """Validation of price_per_hour."""
        while True:
            try:
                price_per_hour = float(input(PromptsConfig.INPUT_PRICE))
                return price_per_hour
            except TypeError as error:
                logger.debug(error)
                print(PromptsConfig.NUMBER_INPUT.format("Price per hour") + "\n")

    @staticmethod
    def input_vehicle_type_id() -> str:
        """Validation of vehicle_type id using regular expression."""
        while True:
            type_id = input(PromptsConfig.INPUT_TYPE_ID).strip()
            is_valid_type_id = Regex.input_validation(Regex.TYPE_ID_REGEX, type_id)
            if is_valid_type_id:
                return type_id

    @staticmethod
    def input_parking_slot_number() -> str:
        """Validation of parking_slot no using regular expression."""
        while True:
            parking_slot_no = input(PromptsConfig.INPUT_PARKING_SLOT_NUMBER).strip()
            is_valid_parking_slot_no = Regex.input_validation(Regex.PARKING_SLOT_NUMBER_REGEX, parking_slot_no)
            if is_valid_parking_slot_no:
                return parking_slot_no.upper()

    @staticmethod
    def input_vehicle_number() -> str:
        """Validation of vehicle no using regular expression."""
        while True:
            print(PromptsConfig.VEHICLE_NUMBER_FORMAT + "\n")
            vehicle_number = input(PromptsConfig.VEHICLE_NUMBER_INPUT).strip()
            is_valid_vehicle_number = Regex.input_validation(Regex.VEHICLE_NUMBER_REGEX, vehicle_number)
            if is_valid_vehicle_number:
                return vehicle_number

    @staticmethod
    def input_out_date() -> str:
        """Validation of out_date using regular expression."""
        while True:
            out_date = input(PromptsConfig.CUSTOMER_OUT_DATE_INPUT).strip()
            present = datetime.now()
            try:
                out_date = datetime.strptime(out_date, "%d-%m-%Y")
                if out_date.date() < present.date():
                    print(Config.cannot_input_past_date + "\n")
                else:
                    return out_date.date().strftime("%d-%m-%Y")
            except ValueError:
                print(Config.invalid_input_prompt + "\n")
