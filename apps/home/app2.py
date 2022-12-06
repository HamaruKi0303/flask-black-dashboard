from flask import Blueprint

# Blueprint を作成
bp = Blueprint('app2', __name__)

# 先程 app.py にあった機能「@app.route('/hoge')」を app2.py に移動
@bp.route('/hoge')
def hoge():
    return 'hoge5'