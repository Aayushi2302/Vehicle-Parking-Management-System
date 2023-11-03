"""
    Module for loading prompts from yaml.
"""
import yaml

FILE_PATH = 'src\\config\\statements\\prompts.yaml'

class Config:
    """
        Class for loading promts from yaml.
    """
    @classmethod
    def load(cls) -> None:
        with open(FILE_PATH, 'r') as file:
            data = yaml.safe_load(file)

        # main module prompts
        cls.database_path = data["database_path"]
        cls.logs_file_path = data["logs_file_path"]
        cls.welcome_message = data["welcome_message"]

        # common prompts
        cls.name_input_prompt = data["name_input"]
        cls.mobile_number_prompt = data["mobile_number_input"]
        cls.zero_record_prompt = data["zero_record"]
        cls.cannot_perform_updation_prompt = data["cannot_perform_updation"]
        cls.maximum_login_attempts = data["maximum_login_attempts"]

        # authentication module prompts
        cls.credential_prompt = data["input_credential"]
        cls.username_prompt = data["input_username"]
        cls.user_not_exist_prompt = data["user_not_exist"]
        cls.user_already_exist_prompt = data["user_already_exist"]
        cls.default_password_prompt = data["input_default_password"]
        cls.change_password_prompt = data["change_password"]
        cls.new_password_prompt = data["input_new_password"]
        cls.confirm_password_prompt = data["input_confirm_password"]
        cls.password_not_match_prompt = data["password_not_match"]
        cls.password_change_successful_prompt = data["password_change_successful"]
        cls.wrong_password_prompt = data["wrong_password"]
        cls.login_attempts_left_prompt = data["login_attempts_left"]
        cls.login_attempts_exhausted_prompt = data["login_attempts_exhausted"]
        cls.password_prompt = data["input_password"]
        cls.successful_login_prompt = data["successful_login"]
        cls.no_records_in_authentication_table_prompt = data["no_record_in_authentication_table"]
        cls.print_default_password_prompt = data["print_default_password"]
        cls.no_default_password_prompt = data["no_default_password"]
        
        # admin module prompts
        cls.create_user_credentials_prompt = data["create_user_credentials"]
        cls.not_valid_username_prompt = data["not_valid_username"]
        cls.role_prompt = data["input_role"]
        cls.not_valid_role_prompt = data["not_valid_role"]
        cls.enter_choice_prompt = data["enter_choice"]
        cls.invalid_input_prompt = data["invalid_input"]
        cls.successful_logout_prompt = data["successful_logout"]
        cls.employee_details_input_prompt = data["employee_details_input"]
        cls.employee_name_input_prompt = data["employee_name_input"]
        cls.employee_age_input_prompt = data["employee_age_input"]
        cls.employee_gender_input_prompt = data["employee_gender_input"]
        cls.employee_mobile_no_input_prompt = data["employee_mobile_no_input"]
        cls.employee_email_input_prompt = data["employee_email_input"]
        cls.details_does_not_exist_prompt = data["details_does_not_exist"]
        cls.updating_details_for_inactive_status_prompt = data["update_details_for_inactive_status"]
        cls.details_for_given_employee_prompt = data["details_for_given_employee"]
        cls.new_detail_input_prompt = data["new_detail_input"]
        cls.employee_removal_successful_prompt = data["employee_removal_successful"]
        cls.employee_updation_successful_prompt = data["employee_updation_successful"]
        cls.employee_registration_successful_prompt = data["employee_registration_successful"]
        cls.enter_details_for_updation_prompt = data["enter_details_for_updation"]
        cls.enter_details_for_removal_prompt = data["enter_details_for_removal"]
        cls.cannot_input_past_date = data["cannot_input_past_date"]

        # helpers module prompts
        cls.strong_password_requirements_prompt = data["strong_password_requirements"]
        cls.weak_password_input_prompt = data["weak_password_input"]

        # vehicle_type prompts
        cls.input_type_name_prompt = data["input_type_name"]
        cls.input_price_prompt = data["input_price"]
        cls.input_type_id_prompt = data["input_type_id"]
        cls.vehicle_type_details_updation_successful_prompt = data["vehicle_type_details_updation_successful"]
        cls.vehicle_type_registration_successful_prompt = data["vehicle_type_registration_successful"]
        cls.vehicle_type_removal_successful_prompt = data["vehicle_type_removal_successful"]
        cls.vehicle_type_does_not_exist_prompt = data["vehicle_type_does_not_exist"]
        cls.vehicle_type_already_exist_prompt = data["vehicle_type_already_exist"]
        cls.typeid_does_not_exist_prompt = data["typeid_does_not_exist"]
        cls.current_price_per_hour_prompt = data["current_price_per_hour"]

        # parking_slot prompts
        cls.input_parking_slot_number_prompt = data["input_parking_slot_number"]
        cls.parking_slot_registration_successful_prompt = data["parking_slot_registration_successful"]
        cls.parking_slot_updation_successful_prompt = data["parking_slot_updation_successful"]
        cls.parking_slot_removal_successful_prompt = data["parking_slot_removal_successful"]
        cls.parking_slot_number_already_exist_prompt = data["parking_slot_number_already_exist"]
        cls.parking_slot_number_does_not_exist_prompt = data["parking_slot_number_does_not_exist"]
        cls.parking_slot_activation_successful_prompt = data["parking_slot_activation_successful"]
        cls.parking_slot_deactivation_successful_prompt = data["parking_slot_deactivation_successful"]
        cls.parking_slot_deletion_successful_prompt = data["parking_slot_deletion_successful"]
        cls.parking_slot_already_vacant_prompt = data["parking_slot_already_vacant"]
        cls.parking_slot_inactive_prompt = data["parking_slot_inactive"]
        cls.parking_slot_deleted_prompt = data["parking_slot_deleted"]

        # customer module prompts
        cls.customer_details_input_prompt = data["customer_details_input"]
        cls.vehicle_number_input_prompt = data["vehicle_number_input"]
        cls.customer_creation_successful_prompt = data["customer_creation_successful"]
        cls.customer_already_exist_prompt = data["customer_already_exist"]
        cls.customer_does_not_exist_prompt = data["customer_does_not_exist"]
        cls.customer_updation_successful_prompt = data["customer_updation_successful"]

        # slot_booking module prompts
        cls.customer_out_date_input_prompt = data["customer_out_date_input"]
        cls.input_details_for_slot_booking_prompt = data["input_details_for_slot_booking"]
        cls.vehicleno_not_found_prompt = data["vehicleno_not_found"]
        cls.parking_slot_assigned_prompt = data["parking_slot_assigned"]
        cls.booking_records_not_found_prompt = data["booking_records_not_found"]
        cls.no_updation_for_check_out_vehicle_prompt = data["no_updation_for_check_out_vehicle"]
        cls.slot_booking_updation_successful_prompt = data["slot_booking_updation_successful"]
        cls.input_booking_id_prompt = data["input_booking_id"]
        cls.parking_slot_vacant_prompt = data["parking_slot_vacant"]

        # parking_charges prompts
        cls.print_parking_charges = data["print_parking_charges"]

        # query_executor prompts
        cls.error_while_handling_database_requests_prompt = data["error_while_handling_database_requests"]
        cls.some_unexpected_error_occured = data["some_unexpected_error_occured"]

        # validator prompts
        cls.username_format_prompt = data["username_format"]
        cls.vehicle_number_foramt_prompt = data["vehicle_number_format"]
        cls.number_input_prompt = data["number_input"]
        cls.age_restriction_prompt = data["age_restriction"] 
