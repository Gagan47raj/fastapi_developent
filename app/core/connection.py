from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL, DATABASE_NAME


# establish database connection with fastapi
client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]
