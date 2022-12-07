from flask import Blueprint

# Blueprint を作成
bp = Blueprint('sample_app1', __name__)

@bp.route('/sample_app1')
def sample_app1():
    return '!!  sample_app1  !!'