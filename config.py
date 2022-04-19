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
DROPZONE_MAX_FILE_SIZE = 100
DROPZONE_MAX_FILES = 1
DROPZONE_DEFAULT_MESSAGE = '请将视频文件拖拽到这里上传'

