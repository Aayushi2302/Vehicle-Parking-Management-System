"""Module for handling employee menu related logic and user interactions."""
import logging

from config.app_config import AppConfig
from config.prompts import PromptsConfig
from config.menu import MenuConfig
from controller.employee_controller import EmployeeController
from parking_manager.parking_charges import ParkingCharges
from utils.common import Common

logger = logging.getLogger('employee_handler')

class EmployeeHandler(ParkingCharges):
    """Class for performing employee menu related interactions."""
    @staticmethod
    def employee_menu() -> int:
        """
            Method to handle employee menu.
        """
        employee_obj = EmployeeController()
        common_obj = Common()
        while True:
            print("\n" + MenuConfig.EMPLOYEE_MENU)
            try:
                choice = int(input(PromptsConfig.ENTER_CHOICE))
                match choice:
                    case 1:
                        employee_obj.register_customer()
                    case 2:
                        employee_obj.update_customer_details()
                    case 3:
                        employee_obj.view_customer_details()
                    case 4:
                        employee_obj.view_parking_slot_details()
                    case 5:
                        employee_obj.book_parking_slot()
                    case 6:
                        employee_obj.vacate_parking_slot()
                    case 7:
                        employee_obj.view_booking_details()
                    case 8:
                        EmployeeHandler.view_parking_charges_for_vehicle_type()
                    case 9:
                        common_obj.view_emp_details()
                    case 10:
                        print(PromptsConfig.SUCCESSFUL_LOGOUT + "\n")
                        return AppConfig.maximum_login_attempts
                    case _ :
                        print(PromptsConfig.INVALID_INPUT)
            except ValueError:
                logger.debug(ValueError)
                print(PromptsConfig.INVALID_INPUT + "\n")
