DEBUG=True
USERNAME = 'root'
PASSWORD = '123456'
HOST = '139.196.19.100'
PORT = '3306'
DATABASE = 'cms'
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True