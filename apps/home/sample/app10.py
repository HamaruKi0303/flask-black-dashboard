from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

import os
from flask import Flask, Response, request, jsonify, render_template
from queue import Queue
import time
import datetime
import json
import pickle

from datetime import datetime as dt

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app10', __name__)


# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app10', methods=['GET', 'POST'])
def sample_app10():
    
    # --------------------------------------------
    # param
    #
    segment         = "sample_app10"
    # running_type = "develop"
    running_type    = "master"
    flask_data      = "apps/static/assets/data"
    log_dir_root    = "weight_log"
    # data
    tdatetime = dt.now()
    tstr_day = tdatetime.strftime('%Y%m%d')
    tstr_min = tdatetime.strftime('%Y%m%d-%H%M%S')
    log_dir_name    = tstr_day
    # log dir/file
    log_dir_path = "{}/{}/{}".format(flask_data, log_dir_root, log_dir_name)
    os.makedirs(log_dir_path, exist_ok=True)
    log_file_path = "{}/{}.json".format(log_dir_path, tstr_min)
    
    # -------------------------------------
    # load weight data
    #
    form_data_path = "apps/static/assets/data/category_weight.csv"
    df_weight_data = pd.read_csv(form_data_path)

    if request.method == 'POST':
        # --------------------------------------------
        # request to dict
        #
        dict_form = request.form.to_dict()
        for k, v in dict_form.items():
            logger.info("k:{:<30}, v:{:<20}".format(k, v))
            weight_id, col_name = k.split("_")
            
            df_weight_data.loc[(df_weight_data["id"] == int(weight_id)), col_name] = v
            df_weight_data.to_csv(form_data_path, index=False)

    logger.info("df_weight_data : \n{}".format(df_weight_data))
    dict_list_form = df_weight_data.to_dict('records')
    
    return render_template('sample/app10.html', 
                            segment=segment, 
                            dict_list_form=dict_list_form,
                            running_type=running_type)