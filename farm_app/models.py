from django.db import models
import pymongo
import os
# Create your models here.
username = os.environ.get("MONGO_USER_NAME", "ameym")
password = os.environ.get("MONGO_USER_PASSWORD", "root")
client = pymongo.MongoClient("mongodb+srv://ameym:root@cluster0.3vy1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.farm_setu

