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
bp = Blueprint('sample_app6', __name__)

# 進捗パーセンテージ用キュー
queue = Queue()

# プログレスバーストリーム
@bp.route('/stream')
def stream():
    return Response(event_stream(queue), mimetype='text/event-stream')

# Queueの値を取り出してEventSourceの'progress-item'に出力（100だったら'last-item'イベントに出力）
def event_stream(queue):
    while True:
        persent = queue.get(True)
        logger.info("progress : {}%".format(persent))

        sse_event = 'progress-item'
        if persent == 100:
            sse_event = 'last-item'
        yield "event:{event}\ndata:{data}\n\n".format(event=sse_event, data=persent)

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app6', methods=['GET', 'POST'])
def sample_app6():
    
    segment = "sample_app6"
    # running_type = "develop"
    running_type = "master"
    
    start = datetime.datetime.now()
    dict_form = request.form.to_dict()
    
    # POSTメソッドの場合
    if request.method == 'POST':

        # サンプル用ループ処理（2秒ごとに10パーセントづつ進行）
        for i in range(10,110,10):
            queue.put(i)
            time.sleep(3)
            
    end = datetime.datetime.now()
    elapsed_time = str(end - start)
    
    dict_form["elapsed_time"] = elapsed_time
    logger.info("dict_list_form")
        
    return render_template('sample/app6.html', 
                            dict_form=dict_form, 
                            segment=segment, 
                            running_type=running_type)