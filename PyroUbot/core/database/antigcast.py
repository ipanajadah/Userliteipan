from PyroUbot.core.database import dB, db_path

db = dB_client["db_path"]
user_collection = db["tes.db"]

async def get_user_ids(client_id: int):
    user_ids = await user_collection.find_one({"_id": client_id})
    return user_ids["tes.db"] if user_ids else []
