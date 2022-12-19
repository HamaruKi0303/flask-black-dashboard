import configparser
from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

import os
from flask import Flask, Response, request, jsonify, render_template
from queue import Queue
import time
import datetime
import json
import pickle

import glob
import re
import os

from datetime import datetime as dt

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app13', __name__)


# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理

@bp.route('/sample_app13', methods=['GET', 'POST'])
def sample_app13():

    # --------------------------------------------
    # page param
    #
    segment = "sample_app13"
    # running_type = "develop"
    running_type = "master"
    render_template_path = 'sample/app13.html'

    # --------------------------------------------
    # global param
    #
    config_path = "apps/static/assets/config/example_config.ini"
    config_ini = configparser.ConfigParser()
    config_ini.read(config_path)
    #
    # preview config
    for section in config_ini.sections():
        logger.info("{:-^60}".format(section))
        for k, v in config_ini[section].items():
            logger.info("{:<30} :{:<20}".format(k, v))

    log_file_list = glob.glob(
        config_ini["FLASK"]["data_root_path"] + "/" +
        config_ini["LOG"]["root_name"] + "/**/*.json")

    d_log_dat = {}
    c = ['tstr-min', ]
    df_weight_total = pd.DataFrame(data=None, index=[1], columns=c)
    for i, log_file_path in enumerate(log_file_list):
        with open(log_file_path) as f:
            log_data = json.load(f)

        df = pd.DataFrame(data=None, index=[1], columns=c)
        df["tstr-min"] = log_data["tstr-min"]
        df["tstr-day"] = log_data["tstr-day"]

        count_list = []
        for k, v in log_data.items():
            logger.info("{:<30} :{:<20}".format(k, v))

            split_str = k.split("_")
            if (len(split_str) > 1):
                weight_name, count = split_str
                df[str(count)] = v
                df["weight_name"] = weight_name

        d_log_dat[log_data["tstr-min"]] = count_list
        if (i == 0):
            df_weight_total = df
        else:
            df_weight_total = pd.concat([df_weight_total, df])

    df_weight_total = df_weight_total.reset_index(drop=True)
    df_weight_total = df_weight_total.dropna(how='any')
    print(df_weight_total)
    df_weight_total.to_csv(config_ini["FLASK"]["data_root_path"] + "/" +
                           config_ini["WEIGHT"]["merged_data_name"],
                           index=False)

    dict_list_form = df_weight_total.to_dict('records')

    return render_template(render_template_path,
                           segment=segment,
                           dict_list_form=dict_list_form,
                           running_type=running_type)
