"""Module for handling employee menu related logic and user interactions."""
import logging

from config.prompts import AppConfig
from config.prompts import PromptsConfig
from config.menu import MenuConfig
from controller.employee_controller import EmployeeController
from parking_manager.parking_charges import ParkingCharges
from utils.common import Common

logger = logging.getLogger('employee_handler')

class EmployeeHandler:
    """Class for performing employee menu related interactions."""
    def __init__(self, username: str) -> None:
        print(PromptsConfig.EMPLOYEE_MENU_WELCOME_MESSAGE + "\n")
        self.username = username
        self.employee_obj = EmployeeController()
        self.common_obj = Common()
        self.parking_charges_obj = ParkingCharges()
    
    def employee_menu(self) -> int:
        """Method to handle employee menu."""
        while True:
            print("\n" + MenuConfig.EMPLOYEE_MENU)
            choice = input(PromptsConfig.ENTER_CHOICE)
            match choice:
                case '1':
                    self.employee_obj.register_customer()
                case '2':
                    self.employee_obj.update_customer_details()
                case '3':
                    self.employee_obj.view_customer_details()
                case '4':
                    self.employee_obj.view_parking_slot_details()
                case '5':
                    self.employee_obj.book_parking_slot()
                case '6':
                    self.employee_obj.vacate_parking_slot()
                case '7':
                    self.employee_obj.view_booking_details()
                case '8':
                    self.parking_charges_obj.view_parking_charges_for_vehicle_type()
                case '9':
                    while True:
                        print("\n" + MenuConfig.MANAGE_PROFILE_MENU)
                        menu_profile_choice = input(PromptsConfig.ENTER_CHOICE)
                        match menu_profile_choice:
                            case '1':
                                self.common_obj.view_individual_employee_details(self.username)
                            case '2':
                                self.common_obj.create_new_password(self.username)
                            case '3':
                                break
                            case _:
                                print(PromptsConfig.INVALID_INPUT)
                        self.common_obj.clear_screen()
                case '10':
                    print(PromptsConfig.SUCCESSFUL_LOGOUT + "\n")
                    return AppConfig.MAXIMUM_LOGIN_ATTEMPTS
                case _:
                    print(PromptsConfig.INVALID_INPUT)
            self.common_obj.clear_screen()
