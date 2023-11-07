"""
    Module for authenticating users(both admin and employee) based on their credentials.
    This module is maintains a login attempts count for each user and does not allow more than 3 invalid login.
    Also the password is stored in hashed format and default password is changed on 1st login of user.
"""
import hashlib
import logging
import time
import maskpass

from config.app_config import AppConfig
from config.prompts import PromptsConfig
from config.query import QueryConfig
from controller.admin_controller import AdminController
from controller.handler.admin_handler import AdminHandler
from controller.handler.employee_handler import EmployeeHandler
from database.query_executor import QueryExecutor
from logs.log_config import LogConfig
from utils.common import Common

logger = logging.getLogger('authentication')

class Authentication:
    """Class for authenticating users and providing role based access as per credentials."""
    def __init__(self) -> None:
        self.common_obj = Common()
        self.max_login_attempts = AppConfig.MAXIMUM_LOGIN_ATTEMPTS

    def invalid_login(self) -> None:
        """Method to notify the user about invalid attempts and attempts left for login."""
        logging.debug(LogConfig.INVALID_LOGIN_INFO)
        self.max_login_attempts -= 1
        print(PromptsConfig.LOGIN_ATTEMPTS_LEFT.format(self.max_login_attempts) + "\n")

    def first_login(self, username: str, password: str, input_password: str) -> None:
        """Method for changing default password on first login."""
        logging.debug(LogConfig.FIRST_LOGIN_INFO)
        if input_password != password:
            self.invalid_login()
        else:
            self.common_obj.create_new_password(username)

    def role_based_access(self, role: str) -> None:
        """Method to assign role to user based on the credentials after authentication."""
        logging.debug(LogConfig.SUCCESSFUL_LOGIN_INFO)
        print(PromptsConfig.SUCCESSFUL_LOGIN + "\n")      
        if role == "admin":
            self.max_login_attempts = AdminHandler.admin_menu()
        else:
            self.max_login_attempts = EmployeeHandler.employee_menu()

    def login(self) -> None:
        """Method for authenticating user."""
        while True:
            if self.common_obj.is_admin_registered():
                print(PromptsConfig.NO_ADMIN_FOUND + "\n")
                admin_obj = AdminController()
                admin_obj.register_employee()

            if self.max_login_attempts == 0:
                print(PromptsConfig.LOGIN_ATTEMPTS_EXHAUSTED + "\n")
                self.max_login_attempts = 3
                time.sleep(10)
            else:
                print("\n" + PromptsConfig.INPUT_CREDENTIAL)
                username = input(PromptsConfig.INPUT_USERNAME).strip()
                input_password = maskpass.askpass(
                                            prompt = PromptsConfig.INPUT_PASSWORD, 
                                            mask="*"
                                        ).strip()
                user_data = QueryExecutor.fetch_data_from_database(
                                QueryConfig.FETCH_EMPLOYEE_CREDENTIALS,
                                (username, "active")
                            )
                if not user_data:
                    self.invalid_login()
                else:
                    password = user_data[0][0]
                    role = user_data[0][1]
                    password_type = user_data[0][2]
                    if password_type == "default":
                        self.first_login(username, password, input_password)
                    else:
                        hashed_password = hashlib.sha256(input_password.encode('utf-8')).hexdigest()
                        if hashed_password == password:
                            self.role_based_access(role)
                        else:
                            self.invalid_login()  
   