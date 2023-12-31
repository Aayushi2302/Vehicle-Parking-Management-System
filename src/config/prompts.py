"""Module for storing prompts of the project."""

class AppConfig:
    """This class contains all the constants of the project."""
    DATABASE_PATH = "src\\database\\parking_management.db"
    LOG_FILE_PATH = "src\\logs\\logs.txt"
    MAXIMUM_LOGIN_ATTEMPTS = 3

    # headers constants
    EMP_ID_HEADER = "EMP ID"
    NAME_HEADER = "Name"
    AGE_HEADER = "Age"
    GENDER_HEADER = "Gender"
    MOBILE_NO_HEADER = "Mobile No"
    EMAIL_ADDRESS_HEADER = "Email Address"
    USERNAME_HEADER = "Username"
    ROLE_HEADER = "Role"
    STATUS_HEADER = "Status"
    CUSTOMER_ID_HEADER = "Customer ID"
    VEHICLE_NO_HEADER = "Vehicle No"
    VEHICLE_TYPE_NAME_HEADER = "Vehicle Type Name"
    PARKING_SLOT_NO_HEADER = "Parking Slot No."
    VEHICLE_TYPE_HEADER = "Vehcile Type"
    BOOKING_ID_HEADER = "Booking ID"
    IN_DATE_HEADER = "In Date"
    IN_TIME_HEADER = "In Time"
    OUT_DATE_HEADER = "Out Date"
    OUT_TIME_HEADER = "Out Time"
    HOURS_HEADER = "Hours"
    CHARGES_HEADER = "Charges"
    VEHICLE_TYPE_ID = "Vehicle Type ID"
    PRICE_PER_HOUR = "Price Per Hour"

class PromptsConfig:
    """This class contains all the prompts of the project."""
    # app module prompts
    WELCOME_MESSAGE = "----Welcome to Vehicle Parking Management System----"
    EXIT_MESSAGE = "----Thank you for using the system. Hope you had a great experience----"

    # common prompts
    ENTER_CHOICE = "Enter your choice (in integer) : " 
    INVALID_INPUT = "Invalid input...Try again"
    INPUT_USERNAME = "Username : "
    INPUT_NAME = "Name : "
    INPUT_MOBILE_NUMBER = "Mobile No. : "
    ZERO_RECORD = "0 records found in {} table. Please enter some records!"
    DETAILS_NOT_EXIST = "{} does not exist..."
    NEW_DETAIL_INPUT = "Enter new {}..."
    SUCCESSFUL_LOGOUT = "Logout of the system successful..."
    CANNOT_PERFORM_UPDATION = "Cannot perform updation. Enter correct data..."
    CANNOT_PERFORM_DELETION = "Cannot perform deletion as no details exist..."
    CANNOT_UPDATE_RECORD = "Cannot update record as no details exist..."
    CANNOT_DEACTIVATE = "Cannot deactivate record as no details exist..."

    # authentication module prompts
    INPUT_CREDENTIAL = "Enter your credentials : "
    INPUT_PASSWORD = "Password : "
    SUCCESSFUL_LOGIN = "Login Successful..."
    LOGIN_ATTEMPTS_LEFT= """
        Invalid login...
        Login attempts left : {}
    """
    LOGIN_ATTEMPTS_EXHAUSTED = "Login attempts exhausted! Please login after some time..."
    CHANGE_PASSWORD = "Update your password..."
    INPUT_NEW_PASSWORD = "New Password : "
    INPUT_CONFIRM_PASSWORD = "Confirm Password : "
    PASSWORD_NOT_MATCH = "Password does not match. Please enter your password again!"
    PASSWORD_CHANGE_SUCCESSFUL = "Password changed successfully! Now login with your new password..."
    NO_ADMIN_FOUND = "Admin does not exit. Please create admin..."

    # admin_controller module prompts
    INPUT_EMPLOYEE_DETAILS = "Enter employee details..."
    INPUT_EMPLOYEE_AGE = "Age : "
    INPUT_EMPLOYEE_GENDER = "Enter F for Female and M for Male : "
    INPUT_EMPLOYEE_ROLE = "Enter role : "
    INPUT_EMPLOYEE_EMAIL = "Email Address : "
    USER_ALREADY_EXIST = "{} already exist. Try Again!"
    EMPLOYEE_REGISTRATION_SUCCESSFUL = "Employee registered successfully..."
    NO_DEFAULT_PASSWORD = "No default password exist...Password has been already changed"
    PRINT_DEFAULT_PASSWORD = "The default password for given employee is {}"
    INPUT_DETAILS_FOR_REMOVAL = "Enter below detail to remove record..."
    UPDATE_DETAILS_FOR_INACTIVE_STATUS = "Cannot update details for given record as the record is not active..."
    EMPLOYEE_REMOVAL_SUCCESSFUL = "Employee removed successfully..."
    INPUT_DETAILS_FOR_UPDATION = "Enter below detail to update record..."
    EMPLOYEE_UPDATION_SUCCESSFUL = "Employee details updated successfully..."
    CREATE_USER_CREDENTIALS = "Create user credentials..."
    NOT_VALID_USERNAME = "Please enter a valid username"
    NOT_VALID_ROLE = "Please enter a valid role"
    DETAILS_FOR_GIVEN_EMPLOYEE = "The details for given employee with emp_id : {} are..."
    CANNOT_INPUT_PAST_DATE = "You entered a date that has been already passed. Please enter a valid date for out_date"
    CANNOT_REMOVE_ADMIN = "Admin can never be removed..."
    CANNOT_UPDATE_ADMIN = "Admin details can't be updated..."

    # validator modules prompts
    USERNAME_FORMAT = "Username should be starting with 'user@' followed by lower-case string of length 5 or more"
    CANNOT_CREATE_ADMIN = "You cannot create admin. Please enter some other role"
    AGE_RESTRICTION = "Age should be greater than 15 and less than 60"
    NUMBER_INPUT = "{} is expected to be a number. Please enter correct input"
    VEHICLE_NUMBER_FORMAT = "Vehcile number should be in the format 'MH-02-VD-9874'"

    # helpers module prompts
    STRONG_PASSWORD_REQUIREMENTS = """
        Please enter a password following below requirements:
            1. Password length should be 8 characters or more.
            2. Password must contain at least one uppercase character.
            3. Password must contain at least one lowercase character.
            4. Password must contain at leat one digit.
            5. Password must contain at least one of the given special character : @, #, $, %, &
    """
    WEAK_PASSWORD_INPUT = "You entered a weak password...Please follow mentioned instructions to create a strong password"

    # vehicle_type module prompts
    INPUT_TYPE_NAME = "Enter a category for vehicle : "
    INPUT_PRICE = "Enter price per hour for the category : "
    VEHICLE_TYPE_REGISTRATION_SUCCESSFUL = "Vehicle type registered successfully..."
    VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL = "Vehicle type details updated successfully..."
    VEHICLE_TYPE_REMOVAL_SUCCESSFUL = "Vehicle type removed successfully..."
    INPUT_TYPE_ID = "Type ID : "
    VEHICLE_TYPE_DOES_NOT_EXIST = "Entered vehicle type does not exist or is inactive..."
    VEHCILE_TYPE_ALREADY_EXIST = "Entered vehcile type already exist..."
    TYPEID_DOES_NOT_EXIST = "Entered Type ID does not exist. Please enter correct Type ID..."
    CURRENT_PRICE_PER_HOUR = "Current price per hour is : {}"

    # parking_slot module prompts
    INPUT_PARKING_SLOT_NUMBER = "Parking Slot No. : "
    PARKING_SLOT_REGISTRATION_SUCCESSFUL = "Parking slot number registered successfully..."
    PARKING_SLOT_ACTIVATION_SUCCESSFUL = "Parking slot number activated successfully..."
    PARKING_SLOT_UPDATION_SUCCESSFUL = "Parking slot number details updated successfully..."
    PARKING_SLOT_REMOVAL_SUCCESSFUL = "Parking slot number removed successfully..."
    PARKING_SLOT_NUMBER_ALREADY_EXIST = "Parking slot number already exist. Please enter a new parking slot number..."
    PARKING_SLOT_NUMBER_DOES_NOT_EXIST = "Parking slot number does not exist. Please enter correct parking slot number..."
    PARKING_SLOT_DEACTIVATION_SUCCESSFUL = "Parking slot deactivated successfully..."
    PARKING_SLOT_DELETION_SUCCESSFUL = "Parking slot deleted successfully..."
    PARKING_SLOT_ALREADY_VACANT = "Parking slot is already vacant. Please enter correct parking slot number"
    PARKING_SLOT_INACTIVE = "Parking slot is inactive. Cannot update status"
    PARKING_SLOT_DELETED = "Parking slot is deleted. Cannot update status"
    CANNOT_VACATE_PARKING_SLOT = "Cannot vacate parking slot as no booking details exist..."
    INPUT_DETAIL_TO_VACATE_PARKING_SLOT = "Enter details for vacating parking slot..."

    # employee_controller module prompts
    CUSTOMER_DETAILS_INPUT = "Enter customer details..."
    VEHICLE_NUMBER_INPUT = "Vehicle No. : "
    CUSTOMER_CREATION_SUCCESSFUL = "Customer registered successfully..."
    CUSTOMER_ALREADY_EXIST = "Customer already exist. Please enter new customer..."
    CUSTOMER_DOES_NOT_EXIST = "Customer does not exist with the vehicle no. Please enter correct vehicle no..."
    CUSTOMER_UPDATION_SUCCESSFUL = "Customer data updated successfully..."

    # slot_booking module prompts
    CUSTOMER_OUT_DATE_INPUT = "Enter customer out date as DD-MM-YYYY format : "
    INPUT_DETAILS_FOR_SLOT_BOOKING = "Enter below details of customer for slot booking..."
    VEHCILE_NO_NOT_FOUND = "Record for given vehicle no not exist. Please regsiter the customer first"
    PARKING_SLOT_ASSIGNED = "Parking slot assigned is : {}"
    BOOKING_RECORD_NOT_FOUND = "Booking records for given customer not found. Please book a parking slot..."
    NO_UPDATION_FOR_CHECKOUT_VEHICLE = "Given vehicle has already left parking slot. No updations can be done..."
    SLOT_BOOKING_UPDATION_SUCCESSFUL = "Slot booking data updated successfully..."
    INPUT_BOOKING_ID = "Booking ID : "
    PARKING_SLOT_VACANT = "Parking slot vacanted successfully..."
    VEHICLE_ALREADY_VACATE_PARKING_SLOT = "Vehicle has already vacated parking slot..."

    # parking_charges prompts
    PRINT_PARKING_CHARGES = "Your parking charge is {} for {} hours spent in parking..."

    # query executor module prompts
    INTEGRITY_ERROR_MESSAGE = "You entered data that already exist. Please enter unique data"
    OPERATIONAL_ERROR_MESSAGE = "Something unexpected happened with the Database. Please try again after some time"
    PROGRAMMING_ERROR_MESSAGE = "Something wrong with the code on backend. Please wait while we resolve the issue"
    GENERAL_EXCEPTION_MESSAGE = """
        We are encountering some issue in the backend side. 
        We will be back soon. 
        Thank you for waiting...
    """

    # handler modules prompts
    ADMIN_MENU_WELCOME_MESSAGE = "Welcome to Admin menu...."
    EMPLOYEE_MENU_WELCOME_MESSAGE = "Welcome to Employee menu..."
    PRESS_KEY_TO_CONTINUE = "Press any key to continue..."
