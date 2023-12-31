"""Module for maintaining all the methods or functionalities of Employee."""
import shortuuid

from src.config.prompts import PromptsConfig
from src.config.query import QueryConfig
from src.controller.handler.customer_update_handler import customer_details_update_menu
from src.database.query_executor import QueryExecutor
from src.parking_manager.parking_slots import ParkingSlot
from src.parking_manager.slot_booking import SlotBooking
from src.utils.common import Common
from src.utils.validator.parking_manager_input_validation import ParkingManagerInputValidation
from src.utils.validator.user_input_validation import UserInputValidation

class EmployeeController(SlotBooking):
    """This class contains methods for maintaining all the methods or functionalities of Employee."""
    def __init__(self) -> None:
        self.common_obj = Common()
        self.parking_slot_obj = ParkingSlot()

    def register_customer(self) -> None:
        """Method to register customer.""" 
        print(PromptsConfig.CUSTOMER_DETAILS_INPUT)
        cust_id = "CUST" + shortuuid.ShortUUID().random(length = 5)
        cust_name = UserInputValidation.input_name()
        cust_mobile_number = UserInputValidation.input_mobile_number()
        cust_vehicle_number = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                    (cust_vehicle_number, )
                )
        if data:
            print(PromptsConfig.CUSTOMER_ALREADY_EXIST + "\n")
            return
        print(PromptsConfig.INPUT_TYPE_NAME)
        vehicle_type_data = QueryExecutor.fetch_data_from_database(
                                QueryConfig.FETCH_VEHICLE_TYPE
                            )
        if not vehicle_type_data:
            print(PromptsConfig.ZERO_RECORD.format("vehicle_type"))
            return
        vehicle_type_name = [(vehicle[1],) for vehicle in vehicle_type_data]
        headers = QueryConfig.VEHICLE_TYPE_HEADER
        self.common_obj.display_table(vehicle_type_name, headers)
        choice = int(input(PromptsConfig.ENTER_CHOICE))
        if choice > len(vehicle_type_name) or choice < 1:
            print(PromptsConfig.INVALID_INPUT)
        else:
            type_name = vehicle_type_name[choice-1][0]
            type_id =   QueryExecutor.fetch_data_from_database(
                            QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                            (type_name, )
                        )
            type_id = type_id[0][0]
            is_success = QueryExecutor.save_data_in_database(
                            QueryConfig.CREATE_CUSTOMER,
                            (cust_id, cust_name, cust_mobile_number, cust_vehicle_number, type_id)
                        )
            if is_success:
                print(PromptsConfig.CUSTOMER_CREATION_SUCCESSFUL + "\n")

    def update_customer_details(self) -> None:
        """Method for updating customer details."""
        if not self.view_customer_details():
            print(PromptsConfig.CANNOT_UPDATE_RECORD + "\n")
            return
        customer_details_update_menu()
    
    def view_customer_details(self) -> bool:
        """Method to view customer details."""
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.VIEW_CUSTOMER_DETAIL
                )
        if not data:
            print(PromptsConfig.ZERO_RECORD.format("customer"))
            return False
        else:
            headers = QueryConfig.CUSTOMER_DETAIL_HEADER
            self.common_obj.display_table(data, headers)
            return True
    
    def view_parking_slot_details(self) -> None:
        """Method to view parking slot details."""
        self.parking_slot_obj.view_parking_slot()
