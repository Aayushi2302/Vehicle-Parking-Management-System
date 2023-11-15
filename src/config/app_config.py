"""Module for storing constants of the project."""

class AppConfig:
    """This class contains all the constants of the project."""

    DATABASE_PATH = "src\\database\\parking_management.db"
    LOG_FILE_PATH = "src\\logs\\logs.txt"
    MAXIMUM_LOGIN_ATTEMPTS = 3
    ROLE_ADMIN = "admin"
    PASSWORD_TYPE_DEFAULT = "default"
    PASSWORD_TYPE_PERMANENT = "permanent"
    EMPLOYEE_ROLE_ACTIVE = "active"