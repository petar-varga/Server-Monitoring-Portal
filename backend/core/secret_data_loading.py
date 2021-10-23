from dotenv import load_dotenv
import os

# get the absolute cwd of this file (secret_data_loading.py)
file_directory = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# current local path
if os.name == "nt":
    path = str(file_directory) + "\\.env"
    load_dotenv(dotenv_path= path)
else:
    load_dotenv(dotenv_path= str(file_directory) + "/.env")

# DATABASE INFO
MYSQL_USERNAME_ENV = os.getenv("MYSQL_USERNAME_ENV")
MYSQL_PASSWORD_ENV = os.getenv("MYSQL_PASSWORD_ENV")
MYSQL_SERVER_ENV = os.getenv("MYSQL_SERVER_ENV")
MYSQL_DATABASE_ENV = os.getenv("MYSQL_DATABASE_ENV")