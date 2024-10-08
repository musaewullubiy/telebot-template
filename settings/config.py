import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
NAME_DB = os.getenv('NAME_DB')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)
