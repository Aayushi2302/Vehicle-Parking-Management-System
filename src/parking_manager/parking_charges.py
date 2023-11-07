"""Module for calculating charges for parking."""
from datetime import datetime

from config.prompts import PromptsConfig
from config.query import QueryConfig
from database.query_executor import QueryExecutor
from parking_manager.vehicle_type import VehicleType

class ParkingCharges:
    """This class contains all the methods for calculating charges for parking."""
    def calculate_hours_spent_in_parking(self, in_date: str, in_time: str, out_date: str, out_time: str) -> float:
        """Method to calculate the number of hours spent by vehicle in parking facility."""
        in_date_time = in_date + " " + in_time
        in_date_time_obj = datetime.strptime(in_date_time, "%d-%m-%Y %H:%M")
        out_date_time = out_date + " " + out_time
        out_date_time_obj = datetime.strptime(out_date_time, "%d-%m-%Y %H:%M")
        time_difference = out_date_time_obj - in_date_time_obj
        hours_spent = time_difference.total_seconds() / (60 * 60)
        total_hours_spent = round(hours_spent, 3)
        return total_hours_spent

    def calculate_charges(self, hours_spent: float, booking_id: str) -> float:
        """Method for calculating total charges based on the number of hours spent."""
        type_id =   QueryExecutor.fetch_data_from_database(
                        QueryConfig.FETCH_TYPE_ID_FROM_BOOKING_ID,
                        (booking_id, )
                    )
        type_id = type_id[0][0]
        price_per_hour = QueryExecutor.fetch_data_from_database(
                            QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                            (type_id, )
                        )
        if not any(price_per_hour):
            print(PromptsConfig.VEHICLE_TYPE_DOES_NOT_EXIST + "\n")
            return 0.0
        else:
            price_per_hour = price_per_hour[0][0]
            total_charges = hours_spent * price_per_hour
            total_charges = round(total_charges, 2)
            return total_charges

    @staticmethod
    def view_parking_charges_for_vehicle_type() -> None:
        """Method to view charges for each vehicle type."""
        vehicle_type_obj = VehicleType()
        vehicle_type_obj.view_vehicle_type()
