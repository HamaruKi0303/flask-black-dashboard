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

from datetime import datetime as dt

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app11', __name__)


# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理

@bp.route('/sample_app11', methods=['GET', 'POST'])
def sample_app11():

    # --------------------------------------------
    # page param
    #
    segment = "sample_app11"
    # running_type = "develop"
    running_type = "master"
    render_template_path = 'sample/app10.html'

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

    # -------------------------------------
    # load weight data
    #
    # form_data_path = "apps/static/assets/data/category_weight.csv"
    form_data_path = \
        "{}/{}".format(config_ini["FLASK"]["data_root_path"],
                        config_ini["WEIGHT"]["category_data_name"])
    df_weight_data = pd.read_csv(form_data_path)

    # -------------------------------------
    # Convert dict to records
    #
    logger.info("df_weight_data : \n{}".format(df_weight_data))
    dict_list_form = df_weight_data.to_dict('records')

    return render_template(render_template_path,
                            segment=segment,
                            dict_list_form=dict_list_form,
                            running_type=running_type)
