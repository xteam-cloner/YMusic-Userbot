import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
import sys
from decouple import config

load_dotenv()

# Configuration using getenv and decouple config
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

SESSION_STRING = config("SESSION_STRING")

BOT_USERNAME = getenv("BOT_USERNAME")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 240))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOGGER_ID"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID"))

PREFIX = int(getenv("PREFIX", "!")

RPREFIX = int(getenv("RPREFIX", "$")


# No Need To Edit Below This

LOG_FILE_NAME = "YMusic.txt"
