import logging
import os


def setup_logger():
    """
    Logger setup for NetSniffX.
    Captured packet details logs/packets.log file la save aagum.
    """

    # logs folder illa na create pannum
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("NetSniffXLogger")
    logger.setLevel(logging.INFO)

    # Duplicate logs avoid panna
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler("logs/packets.log")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger