import os
from dotenv import load_dotenv

DEVS = [5596830979]

devs_boong = list(map(int, getenv("devs_boong", "5596830979").split()))
api_id = int(getenv("api_id", "28174304"))
api_hash = getenv("api_hash", "227eae8466b8f68565060906069ca9e5")
bot_token = getenv("bot_token", "7638570657:AAEwdY564GY_VvvMt52YXqjlTouJBe_Sv-Q")
bot_id = int(getenv("bot_id", "7638570657"))
db_name = getenv("db_name", "tes")
log_pic = getenv("log_pic", "https://files.catbox.moe/j9r906.jpg")
def_bahasa = getenv("def_bahasa", "id")
owner_id = int(getenv("owner_id", "5596830979"))
the_cegers = list(
    map(
        int,
        getenv(
            "the_cegers",
            "5596830979",
        ).split(),
    )
)
dump = int(getenv("dump", "-1002678918064"))
bot_username = getenv("bot_username", "Privateuserbot_bot")
log_userbot = int(getenv("log_userbot", "-1002678918064"))
nama_bot = getenv("nama_bot", "private-userbot")
nama_ip = getenv("nama_ip", "PRIVATE USERBOT 12 PRO")
