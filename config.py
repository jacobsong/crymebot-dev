import json
from dotenv import load_dotenv
from os import environ

load_dotenv()

with open("hitbox.json") as f:
    hitboxData = json.load(f)

TOKEN = environ.get("TOKEN")
PREFIX = environ.get("PREFIX")
MONGOURI = environ.get("MONGOURI")
