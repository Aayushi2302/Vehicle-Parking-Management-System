"""Module for stroing log prompts of the project."""

class LogConfig:
    """This class contains all the log prompts."""

    # main logs
    PROJECT_STARTING_INFO = "Starting with vehicle parking management system."
    CREATING_DATABASE_CONNECTION_DEBUG = "Creating database connection."
    LOSING_DATABASE_CONNECTION_DEBUG = "Closing database connection."
    WRONG_FILE_RUN_DEBUG = "Wrong file run. Run main.py for running the program."

    # authentication logs
    FIRST_LOGIN_INFO = "First Login into the system successful.Change password."
    SUCCESSFUL_LOGIN_INFO = "Successful login into the system."
    INVALID_LOGIN_INFO = "Invalid Login into the system."
    SUCCESSFUL_LOGOUT_INFO = "Successful logout of the system."

    # validatior logs
    INVALID_INPUT_EXCEPTION_INFO = "Invalid input by user."

    # query_executer logs
    SUCCESSFUL_AUTHENTICATION_TABLE_CREATION_INFO = "authentication table created successfully."
    DATA_FETCHED_FROM_DATABASE_SUCESSFUL_INFO = "Data fetched from database successfully."
    DATa_SAVED_TO_DATABASE_SUCCESSFUL_INFO =  "Data saved to database successfully."
    SUCCESSFUL_EMPLOYEE_TABLE_CREATION_INFO = "employee table created successfully."
    SUCCESSFUL_VEHICLE_TYPE_TABLE_CREATION_INFO = "vehicle_type table created successfully."
    SUCCESSFUL_PARKING_SLOT_TABLE_CREATION_INFO = "parking_slot table created successfully."
    SUCCESSFUL_CUSTOMER_TABLE_CREATION_INFO = "customer table created successfully."
    SUCCESSFUL_SLOT_BOOKING_TABLE_CREATION_INFO = "slot_booking table created successfully."
