from loguru import logger

logger.add("app.log", rotation="500 MB", retention="7 days", level="INFO")


def get_logger():
    return logger
