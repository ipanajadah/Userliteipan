import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "293062346").split()))

API_ID = int(os.getenv("API_ID", "25544803"))

API_HASH = os.getenv("API_HASH", "e01c80b4dfafff7085f57edbb5a673b0")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7987834818:AAGY3hbgm0SW2ngLoxknuC9nDT0LKhM33bc")

OWNER_ID = int(os.getenv("OWNER_ID", "293062346"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002692266809").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ipanalkenzi:ipanalkenzi@cluster0.tyhf7ap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002692266809"))
