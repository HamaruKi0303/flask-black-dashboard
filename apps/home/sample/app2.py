from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

# Blueprint を作成
bp = Blueprint('sample_app2', __name__)

@bp.route('/sample_app2')
def sample_app2():
    return render_template('sample/app2.html')