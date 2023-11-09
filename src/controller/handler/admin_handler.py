"""Module for handling admin menu related logic and user interactions."""
import logging

from config.app_config import AppConfig
from config.prompts import PromptsConfig
from config.menu import MenuConfig
from controller.admin_controller import AdminController
from parking_manager.parking_status import ParkingStatus
from utils.common import Common

logger = logging.getLogger('admin_handler')

class AdminHandler(ParkingStatus):
    """Class for performing admin menu related interactions."""
    @staticmethod
    def admin_menu() -> int:
        """Method to handle admin menu."""
        admin_obj = AdminController()
        common_obj = Common()
        while True:
            print("\n" + MenuConfig.ADMIN_MENU)
            try:
                choice = int(input(PromptsConfig.ENTER_CHOICE))    
                match choice:
                    case 1:
                        admin_obj.register_employee()
                    case 2:
                        admin_obj.update_employee_details()
                    case 3:
                        admin_obj.view_employee_details()
                    case 4:
                        admin_obj.view_default_password_for_employee()
                    case 5:
                        admin_obj.remove_employee()
                    case 6 :
                        while True:
                            print("\n" + MenuConfig.MANAGE_VEHICLE_TYPE_MENU)
                            try:
                                vehicle_type_choice = int(input(PromptsConfig.ENTER_CHOICE))
                                match vehicle_type_choice:
                                    case 1:
                                        admin_obj.register_vehicle_type()
                                    case 2:
                                        admin_obj.update_vehicle_price_per_hour()
                                    case 3:
                                        admin_obj.view_vehicle_type()
                                    case 4 :
                                        break
                                    case _ :
                                        print(PromptsConfig.INVALID_INPUT)
                            except ValueError:
                                logger.debug(ValueError)
                                print(PromptsConfig.INVALID_INPUT + "\n")
                    case 7 :
                        while True:
                            print("\n" + MenuConfig.MANAGE_PARKING_SLOT_MENU)
                            try:
                                parking_slot_choice = int(input(PromptsConfig.ENTER_CHOICE))
                                match parking_slot_choice:
                                    case 1:
                                        admin_obj.register_or_activate_parking_slot()
                                    case 2:
                                        admin_obj.deactivate_parking_slot()
                                    case 3:
                                        admin_obj.view_parking_slot()
                                    case 4:
                                        admin_obj.remove_parking_slot()
                                    case 5 :
                                        break
                                    case _ :
                                        print(PromptsConfig.INVALID_INPUT)
                            except ValueError:
                                logger.debug(ValueError)
                                print(PromptsConfig.INVALID_INPUT + "\n")
                    case 8 :
                        while True:
                            print("\n" + MenuConfig.VIEW_PARKING_STATUS_MENU + "\n")
                            try:
                                see_status_choice = int(input(PromptsConfig.ENTER_CHOICE))
                                match see_status_choice:
                                    case 1:
                                        AdminHandler.view_current_date_status()
                                    case 2:
                                        AdminHandler.view_current_year_status()
                                    case 3:
                                        AdminHandler.view_total_vehicle_entries()
                                    case 4:
                                        break
                                    case _ :
                                        print(PromptsConfig.INVALID_INPUT)
                            except ValueError:
                                logger.debug(ValueError)
                                print(PromptsConfig.INVALID_INPUT + "\n")
                    case 9 : 
                        common_obj.view_individual_employee_details()
                    case 10 : 
                        print(PromptsConfig.SUCCESSFUL_LOGOUT + "\n")
                        return AppConfig.MAXIMUM_LOGIN_ATTEMPTS
                    case _ :
                        print(PromptsConfig.invalid_input_prompt)
            except ValueError:
                logger.debug(ValueError)
                print(PromptsConfig.invalid_input_prompt + "\n")
