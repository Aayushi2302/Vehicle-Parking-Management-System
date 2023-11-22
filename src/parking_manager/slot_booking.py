"""Module for maintaing functionalities related to parking slot booking."""
import random
import shortuuid

from src.config.prompts import PromptsConfig
from src.config.query import QueryConfig
from src.database.query_executor import QueryExecutor
from src.parking_manager.parking_charges import ParkingCharges
from src.utils.common import Common
from src.utils.validator.parking_manager_input_validation import ParkingManagerInputValidation

class SlotBooking:
    """This class contains methods for maintaing functionalities related to parking slot booking."""
    def __init__(self) -> None:
        self.common_obj = Common()

    def book_parking_slot(self) -> None:
        """Method for booking parking slot."""
        print(PromptsConfig.INPUT_DETAILS_FOR_SLOT_BOOKING)
        booking_id = "BOOK" + shortuuid.ShortUUID().random(length = 5)
        cust_vehicle_no = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO,
                    (cust_vehicle_no, )
                )
        if not data:
            print(PromptsConfig.VEHCILE_NO_NOT_FOUND + "\n")
        else:
            cust_out_date = ParkingManagerInputValidation.input_out_date()
            customer_id = data[0][0]
            type_id = data[0][1]

            curr_date_and_time = self.common_obj.get_current_date_and_time()
            cust_in_date = curr_date_and_time[0]
            cust_in_time = curr_date_and_time[1]
            parking_slot_no = QueryExecutor.fetch_data_from_database(
                                QueryConfig.FETCH_PARKING_SLOT_NO_FOR_BOOKING,
                                (type_id, "vacant")
                              )
            random_index = random.randrange(len(parking_slot_no))
            booking_parking_slot_no = parking_slot_no[random_index][0]
            is_success = QueryExecutor.save_data_in_database(
                            QueryConfig.CREATE_SLOT_BOOKING,
                            (booking_id, customer_id, booking_parking_slot_no, cust_in_date, cust_in_time, cust_out_date)
                        )
            if is_success:
                query_for_updating_parking_slot_status = QueryConfig.UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.format("status")
                is_success =  QueryExecutor.save_data_in_database(
                                query_for_updating_parking_slot_status,
                                ("booked", booking_parking_slot_no)
                            )
                if is_success:
                    print(PromptsConfig.PARKING_SLOT_ASSIGNED.format(booking_parking_slot_no) + "\n")
            
    def view_booking_details(self) -> bool:
        """Method to view booking details."""
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.VIEW_SLOT_BOOKING_DETAIL
                )
        if not data:
            print(PromptsConfig.ZERO_RECORD.format("slot_booking"))
            return False
        else:
            headers = QueryConfig.SLOT_BOOKING_DETAIL_HEADER
            self.common_obj.display_table(data, headers)
            return True
    
    def vacate_parking_slot(self) -> None:
        """Method to vacate parking slot."""
        if not self.view_booking_details():
            print(PromptsConfig.CANNOT_VACATE_PARKING_SLOT + "\n")
            return
        print("\n" + PromptsConfig.INPUT_DETAIL_TO_VACATE_PARKING_SLOT + "\n")
        vehicle_number = ParkingManagerInputValidation.input_vehicle_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_DETAIL_FOR_VACATING_PARKING_SLOT,
                    (vehicle_number, )
                )
        if not data:
            print(PromptsConfig.CUSTOMER_DOES_NOT_EXIST + "\n")
            return
        else:
            booking_id = data[0][0]
            parking_slot_no = data[0][1]
            in_date = data[0][2]
            in_time = data[0][3]

            out_date_time = self.common_obj.get_current_date_and_time()
            out_date = out_date_time[0]
            out_time = out_date_time[1]
            if out_time is not "XX:XX":
                print(PromptsConfig.VEHICLE_ALREADY_VACATE_PARKING_SLOT + "\n")
                return
            parking_charges_obj = ParkingCharges()
            hours_spent = parking_charges_obj.calculate_hours_spent_in_parking(in_date, in_time, out_date, out_time)
            charges = parking_charges_obj.calculate_charges(hours_spent, booking_id)
            if charges == 0.0:
                return
            query_for_parking_slot_updation = QueryConfig.UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.format("status")
            is_success = QueryExecutor.save_data_in_database(
                            query_for_parking_slot_updation,
                            ("vacant", parking_slot_no),
                        )
            if is_success:
                QueryExecutor.save_data_in_database(
                    QueryConfig.UPDATE_DETAIL_FOR_VACATIG_PARKING_SLOT,
                    (out_date, out_time, hours_spent, charges, booking_id)
                )
                print(PromptsConfig.PARKING_SLOT_VACANT + "\n" + PromptsConfig.PRINT_PARKING_CHARGES.format(charges, hours_spent) + "\n")
