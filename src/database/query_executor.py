"""
    Module for performing all the CRUD operations on the tables in the database.
"""
import logging
from sqlite3 import IntegrityError
from sqlite3 import OperationalError
from sqlite3 import ProgrammingError

from config.app_config import AppConfig
from config.prompts import PromptsConfig
from config.query import QueryConfig
from database.db_connector import DatabaseConnection
from logs.log_config import LogConfig

logger = logging.getLogger('query_executor')

class QueryExecutor:
    """This class contains methods for executing database queries fetched from QueryConfig."""
    @staticmethod
    def create_all_tables() -> None:
        """ Method for creating all tables of database."""
        try:
            with DatabaseConnection(AppConfig.DATABASE_PATH) as connection:
                cursor = connection.cursor()
                cursor.execute(QueryConfig.AUTHENTICATION_TABLE_CREATION)
                logger.info(LogConfig.SUCCESSFUL_AUTHENTICATION_TABLE_CREATION_INFO)
                cursor.execute(QueryConfig.EMPLOYEE_TABLE_CREATION)
                logger.info(LogConfig.SUCCESSFUL_EMPLOYEE_TABLE_CREATION_INFO)
                cursor.execute(QueryConfig.CUSTOMER_TABLE_CREATION)
                logger.info(LogConfig.SUCCESSFUL_CUSTOMER_TABLE_CREATION_INFO)
                cursor.execute(QueryConfig.PARKING_SLOT_TABLE_CREATION)
                logger.info(LogConfig.SUCCESSFUL_PARKING_SLOT_TABLE_CREATION_INFO)
                cursor.execute(QueryConfig.VEHICLE_TYPE_TABLE_CREATION)
                logger.info(LogConfig.SUCCESSFUL_VEHICLE_TYPE_TABLE_CREATION_INFO)
                cursor.execute(QueryConfig.SLOT_BOOKING_TABLE_CREATION)
                logger.info(LogConfig.SUCCESSFUL_SLOT_BOOKING_TABLE_CREATION_INFO)
        except OperationalError as error:
            logger.debug(error)
            print(PromptsConfig.OPERATIONAL_ERROR_MESSAGE + "\n")
        except ProgrammingError as error:
            logger.debug(error)
            print(PromptsConfig.PROGRAMMING_ERROR_MESSAGE + "\n")
        except Exception as error:
            logger.debug(error)
            print(PromptsConfig.GENERAL_EXCEPTION_MESSAGE + "\n")

    @staticmethod
    def fetch_data_from_database(query: str, data: tuple = None) -> list:
        """Method to fetch all the data from the database with the query and data passed as parameter."""
        try:
            with DatabaseConnection(AppConfig.DATABASE_PATH) as connection:
                cursor = connection.cursor()
                if not data:
                    cursor.execute(query)
                else:
                    cursor.execute(query, data)
                data = cursor.fetchall()
                logger.info(LogConfig.DATA_FETCHED_FROM_DATABASE_SUCESSFUL_INFO)
                return data
        except IntegrityError as error:
            logger.debug(error)
            print(PromptsConfig.INTEGRITY_ERROR_MESSAGE + "\n")
        except OperationalError as error:
            logger.debug(error)
            print(PromptsConfig.OPERATIONAL_ERROR_MESSAGE + "\n")
        except ProgrammingError as error:
            logger.debug(error)
            print(PromptsConfig.PROGRAMMING_ERROR_MESSAGE + "\n")
        except Exception as error:
            logger.debug(error)
            print(PromptsConfig.GENERAL_EXCEPTION_MESSAGE + "\n")
     
    @staticmethod
    def save_data_in_database(query: str, data: tuple) -> bool:
        """Method to save data to database with query and data passed as parameter."""
        try:
            with DatabaseConnection(AppConfig.DATABASE_PATH) as connection:
                cursor = connection.cursor()
                cursor.execute(query, data)
                connection.commit()
                logger.info(LogConfig.DATA_SAVED_TO_DATABASE_SUCCESSFUL_INFO)
                return True
        except IntegrityError as error:
            logger.debug(error)
            print(PromptsConfig.INTEGRITY_ERROR_MESSAGE + "\n")
        except OperationalError as error:
            logger.debug(error)
            print(PromptsConfig.OPERATIONAL_ERROR_MESSAGE + "\n")
        except ProgrammingError as error:
            logger.debug(error)
            print(PromptsConfig.PROGRAMMING_ERROR_MESSAGE + "\n")
        except Exception as error:
            logger.debug(error)
            print(PromptsConfig.GENERAL_EXCEPTION_MESSAGE + "\n")
        return False
