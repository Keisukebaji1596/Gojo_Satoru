from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="1874070588 1432756163 1344569458 1789859817 5276098631",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="1344569458",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="1344569458",
        ).split(" ")
    ]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6256462468:AAEzSbfNxONaeJeYdbDrbwdxNbtoeLcFhAU"
    API_ID =  26959103 # Your APP_ID from Telegram
    API_HASH = "ebe24f37c6f8ee727fc406c68ba5bc70"  # Your APP_HASH from Telegram
    OWNER_ID = 5657218265  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001857365749  # Your Private Group ID for logs
    DEV_USERS = [5657218265]
    SUDO_USERS = [5657218265]
    WHITELIST_USERS = [5657218265]
    DB_URI = "mongodb+srv://Anshul0554:Anshul0554@cluster0.uwx7fnj.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "Cluster0"  # Your DB name
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "HentaiAssociation"
    SUPPORT_CHANNEL = "HentaiAssociation"
    VERSION = "5"
    WORKERS = 8
