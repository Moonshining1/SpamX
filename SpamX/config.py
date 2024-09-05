import os
from os import getenv as env
from SpamX.functions.logger import LOGS
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(env("API_ID", "25614292"))
if API_ID is None:
    LOGS.error("Please set your API_ID!")
    quit(1)

API_HASH = str(env("API_HASH", "59ee8005ce6b056fa639d956f028eeeb"))
if API_HASH is None:
    LOGS.error("Please set your API_HASH!")
    quit(1)

ASSISTANT_TOKEN = str(env("ASSISTANT_TOKEN", "6507210376:AAEIpz1aOzQ8WLg7MDUjg858eygO-CiDyLo"))
if ASSISTANT_TOKEN is None:
    LOGS.error("Please set your ASSISTANT_TOKEN!")
    quit(1)

OWNER_ID = int(env("OWNER_ID", "6723933089"))
if OWNER_ID is None:
    LOGS.error("Please set your OWNER_ID!")
    quit(1)

DATABASE_URL = str(env("DATABASE_URL", "postgresql://xrlkskby:gobwyeqocauwmdrggqom@alpha.mkdb.sh:5432/rjfvbvce"))
if DATABASE_URL is None:
    LOGS.error("Please set your DATABASE_URL!")
    quit(1)

LOGGER_ID = str(env("LOGGER_ID", "-1002177358647"))
if LOGGER_ID is None:
    LOGS.error("Please set your LOGGER_ID! (make a private group add assistant in that group & promote as Admin!)")
    quit(1)

# --- ETC
HANDLER = env("HANDLER", ".")
PING_MSG = env("PING_MSG", None)
ALIVE_MSG = env("ALIVE_MSG", None)
ALIVE_MEDIA = env("ALIVE_MEDIA", None)
MULTITASK = env("ALIVE_MEDIA", False)
