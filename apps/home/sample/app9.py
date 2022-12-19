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
bp = Blueprint('sample_app9', __name__)


# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app9', methods=['GET', 'POST'])
def sample_app9():

    # --------------------------------------------
    # param
    #
    segment = "sample_app9"
    # running_type = "develop"
    running_type = "master"
    flask_data = "apps/static/assets/data"
    log_dir_root = "weight_log"
    # data
    tdatetime = dt.now()
    tstr_value = tdatetime.strftime('%Y-%m-%dT%H:%M')

    if request.method == 'POST':
        # --------------------------------------------
        # request to dict
        #
        dict_form = request.form.to_dict()

        # convert str 2 date
        tstr = dict_form["logging-time"]
        tdatetime = dt.strptime(tstr, '%Y-%m-%dT%H:%M')
        logger.info("tdatetime : {}".format(tdatetime))

        # convert date 2 str
        tstr_day = tdatetime.strftime('%Y%m%d')
        tstr_min = tdatetime.strftime('%Y%m%d-%H%M%S')

        # set date
        dict_form["tstr-day"] = tstr_day
        dict_form["tstr-min"] = tstr_min

        logger.info("dict_form : {}".format(dict_form))

        # --------------------------------------------
        # detect weight key
        #
        l_dict_key = list(dict_form.keys())
        key_weight = [s for s in l_dict_key if '-' in s]
        logger.info("key_weight : {}".format(key_weight))

        # log dir/file
        log_dir_name = tstr_day
        log_dir_path = "{}/{}/{}".format(flask_data,
                                         log_dir_root, log_dir_name)
        os.makedirs(log_dir_path, exist_ok=True)
        log_file_path = "{}/{}_{}.json".format(
            log_dir_path, tstr_min, key_weight[0])
        logger.info("log_file_path : {}".format(log_file_path))

        if (key_weight):
            with open(log_file_path, 'w') as fp:
                json.dump(dict_form, fp)

    # -------------------------------------
    # weight data regit
    #
    form_data_path = "apps/static/assets/data/category_weight.csv"
    df_weight_data = pd.read_csv(form_data_path)
    df_weight_data["tstr-value"] = tstr_value
    for i in range(len(df_weight_data)):
        logger.info("name : {}".format(df_weight_data["name"][i]))
        for j in range(df_weight_data["step-num"][i]):
            df_weight_data.at[i, '{}'.format(j+1)] =  \
                df_weight_data["first"][i] + j*df_weight_data["step-size"][i]

        # ------------------
        # 2step weight kg
        #
        if (df_weight_data["step-num2"][i] > 0):
            logger.info(
                "2 step weight ---> num : {}".format(df_weight_data["step-num2"][i]))
            for j2 in range(df_weight_data["step-num2"][i]):
                df_weight_data.at[i, '{}'.format(
                    df_weight_data["step-num"][i]+j2+1)] = df_weight_data["first2"][i] + j2*df_weight_data["step-size2"][i]

    logger.info("df_weight_data : \n{}".format(df_weight_data))
    dict_list_form = df_weight_data.to_dict('records')

    return render_template('sample/app9.html',
                           segment=segment,
                           dict_list_form=dict_list_form,
                           running_type=running_type)
