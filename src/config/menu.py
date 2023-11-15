"""Module for storing menu prompts of the project."""

class MenuConfig:
    """This class contains all the menu prompts of the project.""" 
    ADMIN_MENU = """
        You can perform the following tasks :
            1. Register employee
            2. Update employee details
            3. View employee details
            4. View default password for employee
            5. Remove employee
            6. Manage vehicle type and price
            7. Manage parking slots
            8. See status
            9. Manage your profile
            10. Logout
    """
    MANAGE_PROFILE_MENU = """
        You can peform following tasks :
            1. View your details
            2. Update your password
    """
    EMPLOYEE_DETAIL_UPDATE_MENU = """
        You can update the following details :
            1. Employee Name
            2. Employee Age
            3. Employee Gender
            4. Employee Mobile No.
            5. Employee Email Address
            6. Employee Username
            7. Employee Role
            8. Logout from here
    """
    MANAGE_VEHICLE_TYPE_MENU = """
        You can do the following tasks :
            1. Register a vehicle type
            2. Update vehicle price
            3. See vehicle type details
            4. Logout from here
    """
    MANAGE_PARKING_SLOT_MENU = """
        You can do the following tasks :
            1. Add or activate a parking slot
            2. Deactivate parking slot
            3. See parking slots
            4. Remove parking slot
            5. Logout from here
    """
    EMPLOYEE_MENU = """
        You can perform the following tasks :
            1. Register customer
            2. Update customer details
            3. View customer details
            4. View parking slot details
            5. Book a parking slot 
            6. Vacate a parking slot
            7. View Booking Details
            8. View parking charges for vehicle type
            9. View your details
            10. Logout
    """
    CUSTOMER_DETAIL_UPDATE_MENU = """
        You can update the following details :
            1. Customer Name
            2. Customer Mobile No.
            3. Customer Check Out Date
            4. Logout from here 
    """
    VIEW_PARKING_STATUS_MENU = """
        You can view the below parking status :
            1. View current date vehicle entries
            2. View current year vehicle entries
            3. View total vehicle entries
            4. Logout from here
    """