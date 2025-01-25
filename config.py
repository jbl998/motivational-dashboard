import logging
import time
import os

# Global constants
pathCSV = "files/csv/"
pathIMG = "files/img/"
pathLogs = "files/logs_runtime/"


def setup_logging():
    # Create logs folder if not exists
    if not os.path.exists(pathLogs):
        os.makedirs(pathLogs)

    # Get the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M")

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(f"{pathLogs}/{timestamp}.log", encoding="utf-8"),
        ],
    )
