"""Module for maintaing menu for updating customer details."""
import logging

from config.prompts import PromptsConfig
from config.menu import MenuConfig
from config.query import QueryConfig
from database.query_executor import QueryExecutor
from utils.validator.parking_manager_input_validation import ParkingManagerInputValidation
from utils.validator.user_input_validation import UserInputValidation

logger = logging.getLogger('employee_update_handler')

@staticmethod
def customer_details_update_menu() -> None:
    """Method to update customer details."""
    print("\n" + PromptsConfig.INPUT_DETAILS_FOR_UPDATION + "\n")
    cust_vehicle_no = ParkingManagerInputValidation.input_vehicle_number()
    data =  QueryExecutor.fetch_data_from_database(
                QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                (cust_vehicle_no, )
            )
    if not any(data):
        print(PromptsConfig.CUSTOMER_DOES_NOT_EXIST + "\n")
        return
    customer_id = data[0][0]
    while True:
        print(MenuConfig.CUSTOMER_DETAIL_UPDATE_MENU)
        try:
            choice = int(input(PromptsConfig.ENTER_CHOICE))
            match choice:
                case 1:
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Name"))
                    new_data = UserInputValidation.input_name()
                    updated_field = "name"
                case 2:
                    print(PromptsConfig.NEW_DETAIL_INPUT.format("Mobile No."))
                    new_data = UserInputValidation.input_mobile_number()
                    updated_field = "mobile_no"
                case 3:
                    data =  QueryExecutor.fetch_data_from_database(
                                QueryConfig.FETCH_BOOKING_DETAIL_FROM_CUSTOMER_ID,
                                (customer_id, )
                            )
                    if not any(data):
                        print(PromptsConfig.BOOKING_RECORD_NOT_FOUND + "\n")
                        continue
                    curr_booking_data = data[len(data)-1]
                    booking_id = curr_booking_data[0]
                    curr_out_time = curr_booking_data[6]
                    if curr_out_time != "XX:XX":
                        print(PromptsConfig.NO_UPDATION_FOR_CHECKOUT_VEHICLE + "\n")
                    else:
                        print(PromptsConfig.NEW_DETAIL_INPUT.format("Out Date"))
                        new_data = UserInputValidation.input_out_date()
                        query_for_updating_out_date = QueryConfig.UPDATE_SLOT_BOOKING_DETAIL.format("out_date")
                        is_success = QueryExecutor.save_data_in_database(
                                        query_for_updating_out_date,
                                        (new_data, booking_id)
                                    )
                        if is_success:
                            print(PromptsConfig.SLOT_BOOKING_UPDATION_SUCCESSFUL + "\n")
                    continue
                case 4:
                    break
                case _:
                    print(PromptsConfig.INVALID_INPUT)
            query_for_updating_customer_data = QueryConfig.UPDATE_CUSTOMER_DETAIL.format(updated_field)
            is_success = QueryExecutor.save_data_in_database(
                            query_for_updating_customer_data,
                            (new_data, customer_id)
                        )
            if is_success:
                print(PromptsConfig.CUSTOMER_UPDATION_SUCCESSFUL + "\n")
        except ValueError:
            logger.debug(ValueError)
            print(PromptsConfig.INVALID_INPUT + "\n")
