#encoding:utf-8
from flask import Blueprint
bp = Blueprint('front', __name__)
@bp.route('/front')
def index():
    return "这是前台页面"