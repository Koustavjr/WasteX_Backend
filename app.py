from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()


#  URIs
MONGO_URI = str(os.getenv("MONGO_URI"))



# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["hack_database"]
blogs_collection = db["blogs"]
loc_collection = db["location"]



app = FastAPI()

# Your routes and middleware go here
@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}


@app.get("/blogs")
def get_blogs():
    blogs = []
    for blog in blogs_collection.find():
        blog["_id"] = str(blog["_id"])
        blogs.append(blog)
    return {"blogs": blogs}

