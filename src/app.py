"""
    Main module for Vehicle-Parking-Management System. 
    This is the entry point of the project.
"""
import logging

from src.config.prompts import AppConfig
from src.config.menu import MenuConfig
from src.config.prompts import PromptsConfig
from src.config.query import QueryConfig
from src.database.query_executor import QueryExecutor
from src.logs.log_config import LogConfig
from src.utils.authentication import Authentication

# initializing logger for recording logs
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level = logging.DEBUG,
    filename = AppConfig.LOG_FILE_PATH
)
logger = logging.getLogger('main')

# for creating tables in database
QueryExecutor.create_all_tables()

if __name__ == "__main__":
    logger.info(LogConfig.PROJECT_STARTING_INFO)
    print(PromptsConfig.WELCOME_MESSAGE)

    # for user authentication and granting role based access
    authentication_obj = Authentication()
    authentication_obj.login()
else:
    logger.debug(LogConfig.WRONG_FILE_RUN_DEBUG)
