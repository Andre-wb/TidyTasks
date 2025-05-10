from dotenv import load_dotenv
import os
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SQLALCHEMY_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
