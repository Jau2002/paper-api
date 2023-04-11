from pymongo import MongoClient
from dotenv_vault import load_dotenv
from os import getenv

load_dotenv()

env: list[str] = ["MONGO_USER", "MONGO_PASS", "MONGO_HOST", "MONGO_PORT", "MONGO_DB"]

mongo_user, mongo_pass, mongo_host, mongo_port, mongo_db = (getenv(var) for var in env)

MONGO_URL: str = (
    f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/{mongo_db}"
)


client = MongoClient(MONGO_URL)[mongo_db]
