from flask import Blueprint, request, jsonify, render_template, g

import config
from decorators import login_required
from werkzeug.utils import secure_filename
from models import VideoModel
from exts import db
import uuid  # 用于生成随机字符串
import os

bp = Blueprint('video', __name__, url_prefix='/video')


@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        f = request.files['file']
        if f.filename.split('.')[1] != 'mp4':
            return '目前只接受mp4文件!', 400  # return the error message, with a proper 4XX code
        filename = secure_filename(f.filename)
        extension = filename.rsplit('.')[-1]
        # 生成一个uuid作为文件名
        uuid_name = str(uuid.uuid4()) + "." + extension
        # os.path.join拼接地址，上传地址，f.filename获取文件名
        f.save(os.path.join(config.UPLOAD_FOLDER, uuid_name))
        video_model = VideoModel.query.filter_by(user_id=g.user.id).first()
        if video_model is None:
            video_model = VideoModel(uiid = uuid_name, name = filename, user_id = g.user.id)
            db.session.add(video_model)
            db.session.commit()
        else:
            # 上传新的视频后，将原来的视频删除
            # 判断文件是否存在,文件存在则删除
            if os.path.exists(os.path.join(config.UPLOAD_FOLDER, video_model.uiid)):
                os.remove(os.path.join(config.UPLOAD_FOLDER, video_model.uiid))
            video_model.name = filename
            video_model.uiid = uuid_name
            db.session.commit()
        return jsonify({'code': 200, 'msg': '上传成功'})


# 展示视频
@bp.route('/show', methods=['GET', 'POST'])
@login_required
def show_video():
    if request.method == 'GET':
        return render_template('videos.html')

# 解析视频
@bp.route('/parse', methods=['GET', 'POST'])
@login_required
def parse_video():
    if request.method == 'GET':
        return render_template('parse.html')