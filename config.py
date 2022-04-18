# 数据库的配置信息
HOSTNAME = '101.35.226.193'
PORT = '3306'
DATABASE = 'yolo'
USERNAME = 'yolo'
PASSWORD = 'admin'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'fseafaegeageageag'

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '465'
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = "1361154128@qq.com"
MAIL_PASSWORD = "zasmjzwcujvzgcgc"
MAIL_DEFAULT_SENDER = "1361154128@qq.com"

# 配置上传文件的位置
UPLOAD_FOLDER = 'static/upload'
MAX_CONTENT_LENGTH = 100 * 1024 * 1024 # 100M

