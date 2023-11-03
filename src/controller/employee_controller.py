"""
    Module for maintaining all the methods or functionalities of Employee.
"""
import shortuuid

from config.statements.config import Config
from config.menu.menu_prompts_config import MenuConfig
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from parking_manager.parking_slots import ParkingSlot
from parking_manager.slot_booking import SlotBooking
from utils.common import Common
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation
from utils.validator.user_input_validation import UserInputValidation

class EmployeeController(SlotBooking):
    """
        Class for maintaining all the methods or functionalities of Employee.
    """
    def register_customer(self) -> None:
        """
            Method to register customer.
        """ 
        print(Config.customer_details_input_prompt)
        cust_id = "CUST" + shortuuid.ShortUUID().random(length = 5)
        cust_name = UserInputValidation.input_name()
        cust_mobile_number = UserInputValidation.input_mobile_number()
        cust_vehicle_number = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_customerid_and_typeid_from_vehicleno,
                    (cust_vehicle_number, )
                )
        if any(data):
            print(Config.customer_already_exist_prompt + "\n")
            return
        print(Config.input_type_name_prompt)
        vehicle_type_data = QueryExecutor.fetch_data_from_database(
                                QueryConfig.query_for_fetching_vehicle_type
                            )
        if not any(vehicle_type_data):
            print(Config.zero_record_prompt("vehicle_type"))
            return
        vehicle_type_name = [(vehicle[1],) for vehicle in vehicle_type_data]
        common_obj = Common()
        headers = ["Vehicle Type Name"]
        common_obj.display_table(vehicle_type_name, headers)
        choice = int(input(Config.enter_choice_prompt))
        if choice > len(vehicle_type_name) or choice < 1:
            print(Config.invalid_input_prompt)
        else:
            type_name = vehicle_type_name[choice-1][0]
            type_id =   QueryExecutor.fetch_data_from_database(
                            QueryConfig.query_for_fetching_vehicle_type_typeid_from_typename,
                            (type_name, )
                        )
            type_id = type_id[0][0]
            QueryExecutor.save_data_in_database(
                QueryConfig.query_for_creating_customer,
                (cust_id, cust_name, cust_mobile_number, cust_vehicle_number, type_id),
                Config.customer_creation_successful_prompt + "\n"
            )

    def update_customer_details(self) -> None:
        """
            Module to update customer details.
        """
        self.view_customer_details()
        print("\n" + Config.enter_details_for_updation_prompt + "\n")
        cust_vehicle_no = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_customerid_and_typeid_from_vehicleno,
                    (cust_vehicle_no, )
                )
        if not any(data):
            print(Config.customer_does_not_exist_prompt + "\n")
            return
        customer_id = data[0][0]
        while True:
            print(MenuConfig.customer_detail_update_menu_prompt)
            choice = int(input(Config.enter_choice_prompt))
            match choice:
                case 1:
                    print(Config.new_detail_input_prompt.format("Name"))
                    new_data = UserInputValidation.input_name()
                    updated_field = "name"
                case 2:
                    print(Config.new_detail_input_prompt.format("Mobile No."))
                    new_data = UserInputValidation.input_mobile_number()
                    updated_field = "mobile_no"
                case 3:
                    data =  QueryExecutor.fetch_data_from_database(
                                self.connection,
                                QueryConfig.query_for_fetching_booking_data_with_customer_id,
                                (customer_id, )
                            )
                    if not any(data):
                        print(Config.booking_records_not_found_prompt + "\n")
                        continue
                    curr_booking_data = data[len(data)-1]
                    booking_id = curr_booking_data[0]
                    curr_out_time = curr_booking_data[6]
                    if curr_out_time != "XX:XX":
                        print(Config.no_updation_for_check_out_vehicle_prompt + "\n")
                    else:
                        print(Config.new_detail_input_prompt.format("Out Date"))
                        new_data = UserInputValidation.input_out_date()
                        query_for_updating_out_date = QueryConfig.query_for_updating_slot_booking_details.format("out_date")
                        QueryExecutor.save_data_in_database(
                            self.connection,
                            query_for_updating_out_date,
                            (new_data, booking_id)
                        )
                        print(Config.slot_booking_updation_successful_prompt + "\n")
                    continue
                case 4:
                    break
                case _:
                    print(Config.invalid_input_prompt)
            query_for_updating_customer_data = QueryConfig.query_for_updating_customer_details.format(updated_field)
            QueryExecutor.save_data_in_database(
                query_for_updating_customer_data,
                (new_data, customer_id),
                Config.customer_updation_successful_prompt + "\n"
            )
    
    def view_customer_details(self) -> None:
        """
            Method to view customer details.
        """
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_viewing_customer_details
                )
        if not any(data):
            print(Config.zero_record_prompt.format("customer"))
        else:
            common_obj = Common()
            headers = ["Customer ID", "Name", "Mobile No", "Vehicle No", "Vehicle Type Name"]
            common_obj.display_table(data, headers)
    
    def view_parking_slot_details(self) -> None:
        """
            Method to view parking slot details.
        """
        parking_slot_obj = ParkingSlot()
        parking_slot_obj.view_parking_slot()
    