import logging

# logging.basicConfig(level=logging.NOTSET, filename="example.log",
#                     format="%(asctime)s - %(filename)s - %(levelno)s - %(message)s")
#
# logging.info("be careful")
# logging.warning("oops..")
# logging.critical("hello")

# ============================================================================

# logging.basicConfig(filename="e.log")
#
# a = {"name": "amir"}
#
# try:
#     print(a["age"])
# except Exception:
#     # logging.error("this is error", exc_info=True)
#     logging.exception("this is error")

# =============================================================================

logger = logging.getLogger(__name__)

file_h = logging.FileHandler("example.log")
stream_h = logging.StreamHandler()

file_f = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
stream_f = logging.Formatter("%(levelname)s - %(filename)s - %(message)s")

file_h.setFormatter(file_f)
stream_h.setFormatter(stream_f)

file_h.setLevel(logging.ERROR)
stream_h.setLevel(logging.INFO)

logger.addHandler(file_h)
logger.addHandler(stream_h)

logger.setLevel(logging.INFO)

logger.info("this is a message INFO")
logger.error("this is a message ERROR")
logger.critical("this is a message CRITICAL")
