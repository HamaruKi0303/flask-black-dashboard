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
bp = Blueprint('sample_app8', __name__)


# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app8', methods=['GET', 'POST'])
def sample_app8():
    
    segment = "sample_app8"
    # running_type = "develop"
    running_type = "master"
    
    dict_form = request.form.to_dict()
    pprint.pprint(dict_form)
    
    # -------------------------------------
    # data regit
    #
    form_data_path = "apps/static/assets/data/category_weight.csv"
    df_form = pd.read_csv(form_data_path)
    for i in range(len(df_form)):
        for j in range(df_form["step_num"][i]):
            df_form.at[i, '{}'.format(j+1)] = df_form["first"][i] + j*df_form["step_size"][i]
    
    
    print(df_form)
    dict_list_form = df_form.to_dict('records')
    
    return render_template('sample/app8.html', 
                            segment=segment, 
                            dict_list_form=dict_list_form,
                            running_type=running_type)