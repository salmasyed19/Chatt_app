import os

# For local development
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Syedsallmma19#@localhost/chat"

# For production (Heroku ClearDB)
SQLALCHEMY_DATABASE_URI = os.environ.get("CLEARDB_DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
