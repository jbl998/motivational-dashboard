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


imgInfo = {
    "Futurama": {
        "filename": "last_layoffs_futurama.png",
        "imgwidth": 612,
        "textposition": [{"top": 112, "left": 196}],
        "fontsize": 40,
        "fontcolor": "#9ef8eb"
     },
    "Simpsons": {
        "filename": "last_layoffs_simpsons.png",
        "imgwidth": 612,
        "textposition":[{"top": 125, "left":115}, {"top": 285, "left":100}],
        "fontsize": 50,
        "fontcolor": "#000000"
    },
    "The Office - Darryl": {
        "filename": "last_layoffs_office2.png",
        "imgwidth": 612,
        "textposition": [{"top": 128, "left": 372}],
        "fontsize": 20,
        "fontcolor": "#ccb58d"
    },
    "The Office - Dwight & Jim": {
        "filename": "last_layoffs_office1.png",
        "imgwidth": 612,
        "textposition": [{"top": 140, "left": 210}],
        "fontsize": 25,
        "fontcolor": "#FFFFFF"
    },
}
