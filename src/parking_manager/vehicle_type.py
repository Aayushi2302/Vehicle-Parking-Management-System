"""Module for performing operations related to vehicle_type(like car, truck, etc.) allowed for parking."""
import shortuuid

from src.config.prompts import PromptsConfig
from src.config.query import QueryConfig
from src.database.query_executor import QueryExecutor
from src.utils.common import Common
from src.utils.validator.parking_manager_input_validation import ParkingManagerInputValidation

class VehicleType:
    """This class contains methods for performing operations on vehicle_type."""
    def __init__(self):
        self.common_obj = Common()
    
    def register_vehicle_type(self) -> None:
        """Method for registering a vehicle_type."""
        type_name = ParkingManagerInputValidation.input_vehicle_type_name()
        price_per_hour = ParkingManagerInputValidation.input_price_per_hour()
        data =   QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                    (type_name, )
                )
        if data:
            print(PromptsConfig.VEHCILE_TYPE_ALREADY_EXIST + "\n")
        else:
            type_id = "TYPE" + shortuuid.ShortUUID().random(length = 5)
            is_success = QueryExecutor.save_data_in_database(
                            QueryConfig.CREATE_VEHICLE_TYPE,
                            (type_id, type_name, price_per_hour)
                        )
            if is_success:
                print(PromptsConfig.VEHICLE_TYPE_REGISTRATION_SUCCESSFUL + "\n")
        
    def update_vehicle_price_per_hour(self) -> None:
        """Method for updating vehicle price per hour for parking."""
        if not self.view_vehicle_type():
            print(PromptsConfig.CANNOT_UPDATE_RECORD + "\n")
            return
        print("\n" + PromptsConfig.INPUT_DETAILS_FOR_UPDATION + "\n")
        type_id = ParkingManagerInputValidation.input_vehicle_type_id()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_PRICE_PER_HOUR_FROM_TYPE_ID,
                    (type_id, )
                )
        if not data:
            print(PromptsConfig.TYPEID_DOES_NOT_EXIST + "\n")
            return
        else:
            curr_price_per_hour = data[0][0]
            print(PromptsConfig.CURRENT_PRICE_PER_HOUR.format(curr_price_per_hour) + "\n")
            print(PromptsConfig.NEW_DETAIL_INPUT.format("Price Per Hour"))
            new_data = ParkingManagerInputValidation.input_price_per_hour()
            query = QueryConfig.UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID.format("price_per_hour")
            is_success = QueryExecutor.save_data_in_database(
                            query,
                            (new_data, type_id)
                        )
            if is_success:
                print(PromptsConfig.VEHICLE_TYPE_DETAILS_UPDATION_SUCCESSFUL + "\n")

    def view_vehicle_type(self) -> bool:
        """Method for viewing details of vehicle_type."""
        data = QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_VEHICLE_TYPE
                )
        if not data:
            print(PromptsConfig.ZERO_RECORD.format("vehicle_type"))
            return False
        else:
            headers = QueryConfig.VEHICLE_TYPE_DETAIL_HEADER
            self.common_obj.display_table(data, headers)
            return True
