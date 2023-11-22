"""Module for maintaining parking slot details."""

from src.config.prompts import PromptsConfig
from src.config.query import QueryConfig
from src.database.query_executor import QueryExecutor
from src.utils.common import Common
from src.utils.validator.parking_manager_input_validation import ParkingManagerInputValidation

class ParkingSlot:
    """Thissrc. class contains all methods for maintaining parking slot information."""
    def __init__(self) -> None:
        self.common_obj = Common()

    def register_or_activate_parking_slot(self) -> None:
        """Method to register or activate parking slot."""
        parking_slot_number = ParkingManagerInputValidation.input_parking_slot_number()
        parking_slot_data = QueryExecutor.fetch_data_from_database(
                                QueryConfig.FETCH_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO,
                                (parking_slot_number, )
                            )
        if not parking_slot_data:
            vehicle_type_name = ParkingManagerInputValidation.input_vehicle_type_name()
            vehicle_type_data =  QueryExecutor.fetch_data_from_database(
                                    QueryConfig.FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME,
                                    (vehicle_type_name, )
                                )
            if not vehicle_type_data:
                print(PromptsConfig.VEHICLE_TYPE_DOES_NOT_EXIST + "\n")
                return
            else:
                type_id = vehicle_type_data[0][0]
                is_success = QueryExecutor.save_data_in_database(
                                QueryConfig.CREATE_PARKING_SLOT,
                                (parking_slot_number, type_id)
                             )
                if is_success:
                    print(PromptsConfig.PARKING_SLOT_REGISTRATION_SUCCESSFUL + "\n")
        else:
            status = parking_slot_data[0][2]
            if status == "vacant":
                print(PromptsConfig.PARKING_SLOT_ALREADY_VACANT + "\n")
                return
            else:
                query_for_updating_parking_slot_status = QueryConfig.UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.format("status")
                is_success = QueryExecutor.save_data_in_database(
                                query_for_updating_parking_slot_status,
                                ("vacant", parking_slot_number),
                            )
                if is_success:
                    print(PromptsConfig.PARKING_SLOT_ACTIVATION_SUCCESSFUL + "\n")
        
    def deactivate_parking_slot(self) -> None:
        """Method to deactivate aprking slot."""
        if not self.view_parking_slot():
            print(PromptsConfig.CANNOT_DEACTIVATE + "\n")
            return
        print("\n" + PromptsConfig.INPUT_DETAILS_FOR_UPDATION + "\n")
        parking_slot_number = ParkingManagerInputValidation.input_parking_slot_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO,
                    (parking_slot_number, )
                )
        if not data:
            print(PromptsConfig.PARKING_SLOT_NUMBER_DOES_NOT_EXIST + "\n")
            return
        status = data[0][2]
        if status == "inactive":
            print(PromptsConfig.UPDATE_DETAILS_FOR_INACTIVE_STATUS + "\n")
        else:
            query_for_updating_parking_slot_status = QueryConfig.UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.format("status")
            is_success = QueryExecutor.save_data_in_database(
                            query_for_updating_parking_slot_status,
                            ("inactive", parking_slot_number)
                        )
            if is_success:
                print(PromptsConfig.PARKING_SLOT_DEACTIVATION_SUCCESSFUL + "\n")

    def view_parking_slot(self) -> bool:
        """Method to view parking slot details."""
        parking_slot_data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.VIEW_PARKING_SLOT_DETAIL
                )
        if not parking_slot_data:
            print(PromptsConfig.ZERO_RECORD.format("parking_slot"))
            return False
        else:
            headers = QueryConfig.PARKING_SLOT_DETAIL_HEADER
            self.common_obj.display_table(parking_slot_data, headers)
            return True

    def remove_parking_slot(self) -> None:
        """Method to remove parking slot."""
        if not self.view_parking_slot():
            print(PromptsConfig.CANNOT_PERFORM_DELETION + "\n")
            return
        print("\n" + PromptsConfig.INPUT_DETAILS_FOR_UPDATION + "\n")
        parking_slot_number = ParkingManagerInputValidation.input_parking_slot_number()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.FETCH_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO,
                    (parking_slot_number, )
                )
        if not data:
            print(PromptsConfig.PARKING_SLOT_NUMBER_DOES_NOT_EXIST + "\n")
            return
        query_for_deleting_parking_slot = QueryConfig.UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO.format("status")
        is_success = QueryExecutor.save_data_in_database(
                        query_for_deleting_parking_slot,
                        ("deleted", parking_slot_number, )
                    )
        if is_success:
            print(PromptsConfig.PARKING_SLOT_DELETION_SUCCESSFUL + "\n")
