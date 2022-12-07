from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app3', __name__)

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app3', methods=['GET', 'POST'])
def sample_app3():
    
    segment = "sample_app3"
    
    form_data_path = "apps/static/assets/data/form_data.csv"
    df_form = pd.read_csv(form_data_path, index_col=0)
    
    # POSTメソッドの場合
    if request.method == 'POST':

        dict_form = request.form.to_dict()
        df_form = df_form.append(dict_form, ignore_index=True)
        
        logger.info("df_form")
        df_form.to_csv(form_data_path)
        pprint.pprint(df_form)
        
    logger.info("dict_list_form")
    dict_list_form = df_form.to_dict('records')
    pprint.pprint(dict_list_form)
    # name = request.form['name']
        
    return render_template('sample/app3.html', dict_list_form=dict_list_form, segment=segment)