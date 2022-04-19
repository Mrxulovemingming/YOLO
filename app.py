from flask import Flask, render_template, session, g, send_from_directory
import config
from exts import db, mail
from blueprints import user_bp
from blueprints import video_bp
from flask_migrate import Migrate
from models import UserModel, VideoModel
from flask_dropzone import Dropzone

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)
drop_zone = Dropzone()
drop_zone.init_app(app)
app.register_blueprint(user_bp)
app.register_blueprint(video_bp)

@app.before_request
def before_request():
    if session.__contains__("user_id"):
        user_id = session['user_id']
        if user_id:
            try:
                user_model = UserModel.query.get(user_id)
                g.user = user_model
                video_model = VideoModel.query.filter_by(user_id=user_id).first()
                if video_model:
                    g.video = video_model
            except:
                g.user = None
                g.video = None


@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}


@app.context_processor
def video_context_processor():
    if hasattr(g, 'video'):
        return {'video': g.video}
    else:
        return {}


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
