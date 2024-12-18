from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "mydatabase"

client = None

async def get_db():
    global client
    if client is None:
        client = AsyncIOMotorClient(MONGO_URI)
    return client[DATABASE_NAME]
