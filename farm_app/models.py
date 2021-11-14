from django.db import models
import pymongo

# Create your models here.
client = pymongo.MongoClient("mongodb+srv://ameym:root@cluster0.3vy1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.farm_setu

