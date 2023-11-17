"""Module for maintaing menu for updating employee details."""
import logging

from config.prompts import PromptsConfig
from config.menu import MenuConfig
from config.query import QueryConfig
from database.query_executor import QueryExecutor
from utils.common import Common
from utils.validator.user_input_validation import UserInputValidation

logger = logging.getLogger('employee_update_handler')

def employee_details_update_menu() -> None:
    """Method for updating employee details."""
    common_obj = Common()
    print("\n" + PromptsConfig.INPUT_DETAILS_FOR_UPDATION + "\n")
    emp_email = UserInputValidation.input_email_address()
    data =  QueryExecutor.fetch_data_from_database(
                QueryConfig.FETCH_EMP_ID_STATUS_AND_ROLE_FROM_EMAIL,
                (emp_email, )
            )
    if not data:
        print(PromptsConfig.DETAILS_NOT_EXIST.format(emp_email))
        return
    emp_id = data[0][0]
    emp_status = data[0][1]
    role = data[0][2]
    if role == "admin":
        print(PromptsConfig.CANNOT_UPDATE_ADMIN + "\n")
        return
    if emp_status == "inactive":
        print(PromptsConfig.UPDATE_DETAILS_FOR_INACTIVE_STATUS + "\n")
    else:
        while True:
            print(MenuConfig.EMPLOYEE_DETAIL_UPDATE_MENU)
            choice = input(PromptsConfig.ENTER_CHOICE)
            match choice :
                case '1':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Name"))
                    new_data = UserInputValidation.input_name()
                    updated_field = "name"
                case '2':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Age"))
                    new_data = UserInputValidation.input_age()
                    updated_field = "age"
                case '3':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Gender"))
                    new_data = UserInputValidation.input_gender()
                    updated_field = "gender"
                case '4':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Mobile No."))
                    new_data = UserInputValidation.input_mobile_number()
                    updated_field = "mobile_no"
                case '5':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Email Address"))
                    new_data = UserInputValidation.input_email_address()
                    updated_field = "email_address"
                case '6':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Username"))
                    new_data = UserInputValidation.input_username()
                    updated_field = "username"
                case '7':
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Role"))
                    new_data = UserInputValidation.input_role()
                    updated_field = "role"
                case '8': 
                    break
                case _:
                    print(PromptsConfig.INVALID_INPUT)
            if updated_field in ("role", "username"):
                query = QueryConfig.UPDATE_EMPLOYEE_CREDENTIAL_FROM_EMP_ID.format(updated_field)
            else:
                query = QueryConfig.UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID.format(updated_field)
            is_success = QueryExecutor.save_data_in_database(
                            query,
                            (new_data, emp_id)
                        )
            if is_success:
                print(PromptsConfig.EMPLOYEE_UPDATION_SUCCESSFUL + "\n")
            common_obj.clear_screen()
