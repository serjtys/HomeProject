import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

# Настройка логирования для модуля utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

utils_handler = logging.FileHandler("../logs/utils.log")
utils_handler.setLevel(logging.DEBUG)

utils_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
utils_handler.setFormatter(utils_formatter)

utils_logger.addHandler(utils_handler)

# Настройка логирования для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

masks_handler = logging.FileHandler("../logs/masks.log")
masks_handler.setLevel(logging.DEBUG)

masks_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
masks_handler.setFormatter(masks_formatter)

masks_logger.addHandler(masks_handler)
