import logging
import os 
from datetime import datetime

'''
Centralized logging configuration for the TASP/TNN project.

- Creates a shared log file per run in ./logs/
- Provides setup_logger(name) for module-level loggers
- Writes to both file and console
'''


logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(
    logs_path, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
)

# === 2. Configure the root logger (global setup) ===

logging.basicConfig(
    format="[{asctime}] [{levelname}] [{name}] :: {message}",
    style="{",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode="a"),
        logging.StreamHandler(),
    ]
)

# === 3. Provide reusable function for modules ===
def setup_logger(name: str):
    """
    Returns a logger instance with the given name.
    Example:
        logger = setup_logger("tasp.simulator")
    """
    return logging.getLogger(name)


if __name__ == "__main__":
    logger = setup_logger("tasp.test")
    logger.info("Logger test: Initialized successfully.")