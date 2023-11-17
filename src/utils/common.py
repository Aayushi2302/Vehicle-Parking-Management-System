"""Module containing common methods which are shared across the project."""
from datetime import datetime
import hashlib
import logging
import os
import pytz
import maskpass
from tabulate import tabulate

from config.prompts import AppConfig
from config.prompts import PromptsConfig
from config.query import QueryConfig
from database.query_executor import QueryExecutor
from logs.log_config import LogConfig
import utils.regex_pattern as Regex
from utils.validator.user_input_validation import UserInputValidation

logger = logging.getLogger('common')

class Common:
    """This class contain helper methods to be shared throughout the project."""
    def admin_not_registered(self) -> bool:
        """Method for checking whether admin is registered in the database who is the first user of the system."""
        user_data = QueryExecutor.fetch_data_from_database(
                        QueryConfig.FETCH_EMPID_FROM_ROLE_AND_STATUS,
                        ("admin", "active")
                    )
        if not user_data:
            return True
        else:
            return False
    
    def create_new_password(self, username: str) -> str:
        """Method for creating new password for the user following strong password recommendation."""
        while True:
            print(PromptsConfig.CHANGE_PASSWORD + "\n")
            print(PromptsConfig.STRONG_PASSWORD_REQUIREMENTS + "\n")
            input_password = maskpass.askpass(
                                prompt = PromptsConfig.INPUT_NEW_PASSWORD,
                                mask="*"
                            )
            is_strong_password = Regex.input_validation(Regex.PASSWORD_PATTERN, input_password)
            if not is_strong_password:
                print(PromptsConfig.WEAK_PASSWORD_INPUT + "\n")
            else:
                new_password = input_password
                confirm_password = ""
                while True:
                    confirm_password =  maskpass.askpass(
                        prompt = PromptsConfig.INPUT_CONFIRM_PASSWORD,
                        mask="*"
                    )
                    if new_password != confirm_password:
                        print(PromptsConfig.PASSWORD_NOT_MATCH + "\n")
                    else:
                        break
                hashed_password = hashlib.sha256(confirm_password.encode('utf-8')).hexdigest()
                is_success =  QueryExecutor.save_data_in_database(
                                QueryConfig.UPDATE_DEFAULT_PASSWORD,
                                (hashed_password, "permanent", username),
                              )
                if is_success:
                    print(PromptsConfig.PASSWORD_CHANGE_SUCCESSFUL + "\n")
                return

    def view_individual_employee_details(self, username: str) -> None:
        """Method to display a particular user details."""
        print(PromptsConfig.DETAILS_FOR_GIVEN_EMPLOYEE.format(username))
        emp_data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                    (username, )
                )
        headers = QueryConfig.EMPLOYEE_DETAIL_HEADER
        self.display_table(emp_data, headers)

    def display_table(self, data: list, headers: list) -> None:
        """Method to display data in tabular format using tabulate."""
        row_id = [i for i in range(1, len(data) + 1)]
        print(
                tabulate(
                    data,
                    headers,
                    showindex = row_id,
                    tablefmt = "simple_grid"
                )
            )
    
    def get_current_date_and_time(self) -> tuple:
        """For recording current date and time."""
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_time = current.strftime('%H:%M')
        curr_date = current.strftime('%d-%m-%Y')
        return (curr_date, curr_time)
    
    def clear_screen(self) -> None:
        """Method to clear the screen after a task is performed."""
        if input("\n" + PromptsConfig.PRESS_KEY_TO_CONTINUE + "\n"):
            os.system('cls')
