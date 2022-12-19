from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

from flask import Flask, Response, request, jsonify, render_template
from queue import Queue
import time
import datetime
import json

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app7', __name__)


# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app7', methods=['GET', 'POST'])
def sample_app7():
    
    segment = "sample_app7"
    # running_type = "develop"
    running_type = "master"
    
    return render_template('sample/app7.html', 
                            segment=segment, 
                            running_type=running_type)