"""Module for handling admin menu related logic and user interactions."""
import keyboard
import logging

from config.prompts import AppConfig
from config.prompts import PromptsConfig
from config.menu import MenuConfig
from controller.admin_controller import AdminController
from parking_manager.parking_status import ParkingStatus
from utils.common import Common

logger = logging.getLogger('admin_handler')

class AdminHandler:
    """Class for performing admin menu related interactions."""
    def __init__(self, username: str) -> None:
        print(PromptsConfig.ADMIN_MENU_WELCOME_MESSAGE + "\n")
        self.username = username
        self.admin_obj = AdminController()
        self.common_obj = Common()
        self.parking_status_obj = ParkingStatus()

    def admin_menu(self) -> int:
        """Method to handle admin menu."""
        while True:
            print("\n" + MenuConfig.ADMIN_MENU)
            choice = input(PromptsConfig.ENTER_CHOICE)  
            match choice:
                case '1':
                    self.admin_obj.register_employee()
                case '2':
                    self.admin_obj.update_employee_details()
                case '3':
                    self.admin_obj.view_employee_details()
                case '4':
                    self.admin_obj.view_default_password_for_employee()
                case '5':
                    self.admin_obj.remove_employee()
                case '6':
                    while True:
                        print("\n" + MenuConfig.MANAGE_VEHICLE_TYPE_MENU)
                        vehicle_type_choice = input(PromptsConfig.ENTER_CHOICE)
                        match vehicle_type_choice:
                            case '1':
                                self.admin_obj.register_vehicle_type()
                            case '2':
                                self.admin_obj.update_vehicle_price_per_hour()
                            case '3':
                                self.admin_obj.view_vehicle_type()
                            case '4' :
                                break
                            case _ :
                                print(PromptsConfig.INVALID_INPUT)
                        self.common_obj.clear_screen()
                case '7':
                    while True:
                        print("\n" + MenuConfig.MANAGE_PARKING_SLOT_MENU)
                        parking_slot_choice = input(PromptsConfig.ENTER_CHOICE)
                        match parking_slot_choice:
                            case '1':
                                self.admin_obj.register_or_activate_parking_slot()
                            case '2':
                                self.admin_obj.deactivate_parking_slot()
                            case '3':
                                self.admin_obj.view_parking_slot()
                            case '4':
                                self.admin_obj.remove_parking_slot()
                            case '5' :
                                break
                            case _ :
                                print(PromptsConfig.INVALID_INPUT)
                        self.common_obj.clear_screen()
                case '8':
                    while True:
                        print("\n" + MenuConfig.VIEW_PARKING_STATUS_MENU + "\n")
                        see_status_choice = input(PromptsConfig.ENTER_CHOICE)
                        match see_status_choice:
                            case '1':
                                self.parking_status_obj.view_current_date_status()
                            case '2':
                                self.parking_status_obj.view_current_year_status()
                            case '3':
                                self.parking_status_obj.view_total_vehicle_entries()
                            case '4':
                                break
                            case _ :
                                print(PromptsConfig.INVALID_INPUT)
                        self.common_obj.clear_screen()
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
