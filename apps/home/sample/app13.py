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

    # --------------------------------------------
    # adjust merged data 
    #
    merged_data_path = config_ini["FLASK"]["data_root_path"] + "/" + config_ini["WEIGHT"]["merged_data_name"]    
    logger.info("merged_data_path : {}".format(merged_data_path))
    df_merged_data = pd.read_csv(merged_data_path)
    df_merged_data = df_merged_data.reset_index()
    df_merged_data = df_merged_data.rename(columns={'index': 'ID'})
    
    
    # --------------------------------------------
    # analysis
    # 
    df_merged_data["total"] = 0
    for i in range(1, int(config_ini["WEIGHT"]["try_num"])+1):
        df_merged_data["total"] = df_merged_data["total"] + df_merged_data[str(i)]
    
    logger.info("df_merged_data : \n{}".format(df_merged_data))
    
    chart_dcit = {}
    target_weight_name = "Abdominal-Crunch"
    target_df_merged_data = df_merged_data[df_merged_data["weight_name"] == target_weight_name]
    logger.info("target_df_merged_data : \n{}".format(target_df_merged_data))
    target_df_merged_data = target_df_merged_data.drop(['ID', 'tstr-min', 'tstr-day', 'weight_name', 'total'], axis=1)
    logger.info("target_df_merged_data : \n{}".format(target_df_merged_data))
    chart_dcit[target_weight_name] = {}
    chart_dcit[target_weight_name]["x"] = list(range(len(target_df_merged_data.values.reshape(-1))))
    chart_dcit[target_weight_name]["y"] = list(target_df_merged_data.values.reshape(-1))
    
    pprint.pprint(chart_dcit)
    
    
    dict_list_form = df_merged_data.to_dict('records')

    return render_template(render_template_path,
                           segment=segment,
                           dict_list_form=dict_list_form,
                           chart_dcit=chart_dcit,
                           running_type=running_type)
