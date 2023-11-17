"""Module for maintaing methods for showing booking status to admin."""
from datetime import datetime
import pytz

from config.prompts import PromptsConfig
from config.query import QueryConfig
from database.query_executor import QueryExecutor
from parking_manager.slot_booking import SlotBooking
from utils.common import Common

class ParkingStatus:
    """This class contains methods for displaying different booking status to admin."""
    def __init__(self) -> None:
        self.common_obj = Common()
        self.slot_booking_obj = SlotBooking()

    def view_current_date_status(self) -> None:
        """Method for view current date booking status."""
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_date = current.strftime('%d-%m-%Y')
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_CURRENT_DATE_RECORD,
                    (curr_date, )
                )
        if not data:
            print(PromptsConfig.ZERO_RECORD.format("booking") + "\n")
        else:
            headers = QueryConfig.SLOT_BOOKING_DETAIL_HEADER
            self.common_obj.display_table(data, headers)
            
    def view_current_year_status(self) -> None:
        """Method to see current year booking details."""
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_year = int(current.strftime('%Y'))
        curr_year_query = f"%-%-{curr_year}"
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_CURRENT_YEAR_RECORD,
                    (curr_year_query, )
                )
        if not data:
            print(PromptsConfig.ZERO_RECORD.format("booking") + "\n")
        else:
            headers = QueryConfig.SLOT_BOOKING_DETAIL_HEADER
            self.common_obj.display_table(data, headers)

    def view_total_vehicle_entries(self) -> None:
        """Method to display total booking status till current date."""
        self.slot_booking_obj.view_booking_details()
