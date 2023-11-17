"""Module for maintaining all the methods or functionalities of Admin."""
import random
import string
import shortuuid

from config.prompts import PromptsConfig
from config.query import QueryConfig
from controller.handler.employee_update_handler import employee_details_update_menu
from database.query_executor import QueryExecutor
from parking_manager.parking_slots import ParkingSlot
from parking_manager.vehicle_type import VehicleType
from utils.common import Common
from utils.validator.user_input_validation import UserInputValidation

class AdminController(VehicleType, ParkingSlot):
    """
        This class contains all the functionalities that user can perform on Employee.
        Also this class inherits VehicleType and ParkingSlot class to implement further admin functionalities.
    """
    def __init___(self) -> None:
        self.common_obj = Common()

    def register_employee(self, role: str = None) -> None:
        """Method to register employee and save their data to database."""
        print(PromptsConfig.INPUT_EMPLOYEE_DETAILS + "\n")
        emp_id = "EMP" + shortuuid.ShortUUID().random(length = 5)
        emp_name = UserInputValidation.input_name()
        emp_username = UserInputValidation.input_username()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_EMPID_FROM_USERNAME,
                    (emp_username, )
                )
        if data:
            print(PromptsConfig.USER_ALREADY_EXIST.format(emp_username) + "\n")
        else:
            characters = string.ascii_letters + string.digits + "@#$&%"
            emp_password = ''.join(random.choice(characters) for _ in range(8))
            emp_age = UserInputValidation.input_age()
            emp_gender = UserInputValidation.input_gender()
            emp_role = UserInputValidation.input_role(role)
            emp_mobile_number = UserInputValidation.input_mobile_number()
            emp_email_address = UserInputValidation.input_email_address()
            data =  QueryExecutor.fetch_data_from_database(
                        QueryConfig.FETCH_EMP_ID_FROM_EMAIL,
                        (emp_email_address, )
                    )
            if data:
                print(PromptsConfig.USER_ALREADY_EXIST.format(emp_email_address) + "\n")
            else:
                is_success = QueryExecutor.save_data_in_database(
                                QueryConfig.CREATE_EMPLOYEE_CREDENTIALS,
                                (emp_id, emp_username, emp_password, emp_role)
                            )
                if is_success:
                    QueryExecutor.save_data_in_database(
                        QueryConfig.CREATE_EMPLOYEE_DETAILS,
                        (emp_id, emp_name, emp_age, emp_gender, emp_mobile_number, emp_email_address)
                    )
                    print(PromptsConfig.EMPLOYEE_REGISTRATION_SUCCESSFUL + "\n")

    def update_employee_details(self) -> None:
        """Method to update employee details."""
        if not self.view_employee_details():
            print(PromptsConfig.CANNOT_UPDATE_RECORD + "\n")
            return
        employee_details_update_menu()
                          
    def view_employee_details(self) -> bool:
        """Method to display employee details."""
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.VIEW_EMPLOYEE_DETAIL
                )
        if not data:
            print(PromptsConfig.ZERO_RECORD.format("employee"))
            return False
        else:
            headers = QueryConfig.EMPLOYEE_DETAIL_HEADER
            self.common_obj.display_table(data, headers)
            return True

    def view_default_password_for_employee(self) -> None:
        """Method to display default password of employee to admin."""
        emp_email = UserInputValidation.input_email_address()
        emp_id = QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_FROM_EMAIL,
                    (emp_email, )
                )
        if not emp_id:
            print(PromptsConfig.DETAILS_NOT_EXIST.format(emp_email) + "\n")
        else:
            emp_id = emp_id[0][0]
            data =  QueryExecutor.fetch_data_from_database(
                        QueryConfig.FETCH_DEFAULT_PASSWORD_FROM_EMPID,
                        (emp_id, )
                    )
            password_type = data[0][0]
            default_password = data[0][1]
            if password_type == "permanent":
                print(PromptsConfig.NO_DEFAULT_PASSWORD + "\n")
            else:
                print(PromptsConfig.PRINT_DEFAULT_PASSWORD.format(default_password) + "\n")

    def remove_employee(self) -> None:
        """Method to remove or inactivate the employee."""
        if not self.view_employee_details():
            print(PromptsConfig.CANNOT_PERFORM_DELETION + "\n")
            return
        print("\n" + PromptsConfig.INPUT_DETAILS_FOR_REMOVAL + "\n")
        emp_email = UserInputValidation.input_email_address()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_EMP_ID_STATUS_AND_ROLE_FROM_EMAIL,
                    (emp_email, )
                )
        if not data:
            print(PromptsConfig.DETAILS_NOT_EXIST.format(emp_email) + "\n")
            return
        emp_id = data[0][0]
        status = data[0][1]
        role = data[0][2]
        if role == "admin":
            print(PromptsConfig.CANNOT_REMOVE_ADMIN + "\n")
            return
        if status == "inactive":
            print(PromptsConfig.UPDATE_DETAILS_FOR_INACTIVE_STATUS)
        else:
            query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format("status")
            is_success = QueryExecutor.save_data_in_database(
                            query,
                            ("inactive", emp_id)
                        )
            if is_success:
                print(PromptsConfig.EMPLOYEE_REMOVAL_SUCCESSFUL + "\n")
