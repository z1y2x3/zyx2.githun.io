# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zlckqa'
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "sdfsadfskrwerfj1233453345"

# 邮箱配置
# 我们项目中用的是QQ邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "2286408956@qq.com"
MAIL_PASSWORD = "elpuncwclqsiebeh"
MAIL_DEFAULT_SENDER = "2286408956@qq.com"
