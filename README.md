
# FLASK dashboard

![](https://i.imgur.com/SsY476Z.png)

# Index

- [1. Introduction](#1-introduction)
- [2. Updates!!](#2-updates)
- [3. Coming soon](#3-coming-soon)
- [4. Quick Start](#4-quick-start)
  - [4.1. ✨ Start the app in Docker](#41--start-the-app-in-docker)
- [5. Detail](#5-detail)
  - [5.1. ✨ フォルダ構成](#51--フォルダ構成)
- [6. Sample basic site](#6-sample-basic-site)
  - [6.1. Simple text page](#61-simple-text-page)
  - [6.2. Simple HTML page](#62-simple-html-page)
  - [6.3. POST page](#63-post-page)
  - [6.4. Active sidebar](#64-active-sidebar)
  - [6.5. Switch sidebar](#65-switch-sidebar)
  - [6.6. Simple progress bar](#66-simple-progress-bar)
  - [6.7. Add new page](#67-add-new-page)
- [7. Sample chart site](#7-sample-chart-site)
  - [7.1. Simple chart](#71-simple-chart)
  - [7.2. Radio \& Date form page](#72-radio--date-form-page)
  - [7.3. Index page](#73-index-page)
  - [7.4. Config update page](#74-config-update-page)
  - [7.5. Config parser page](#75-config-parser-page)
  - [7.6. Table preview page](#76-table-preview-page)
  - [7.7. Visual page](#77-visual-page)
- [8. Reference site](#8-reference-site)
- [9. memo](#9-memo)

## 1. Introduction

`FLASK`製のダッシュボードのテンプレートです．

基本的に使用するであろう，POSTの通信部分とデータの描画，新規ページの追加，サイドバー付近を開発できるようにサンプルのサイトを作成しました．

このサンプルサイトを複製し，元にすれば開発効率がアップすること間違いなしです．

https://github.com/HamaruKi0303/flask-black-dashboard

## 2. Updates!!
* 【2022/12/05】[元のサイト](https://github.com/app-generator/flask-black-dashboard)のフォーク & base `README.md` の追加
* 【2022/12/07】[サンプルサイト](#6-sample-site)：app1~app5を作成
* 【2022/12/15】[Simple progress bar](#66-simple-progress-bar)：app6を作成
* 【2022/12/15】[Add new page](#67-add-new-page)
* 【2022/12/16】[Demo chart page](#67-add-new-page) : app7を作成
* 【2022/12/17】[Radio & date form page](#67-add-new-page) : app8を作成
* 【2022/12/18】[Index page](#67-add-new-page) : app9を作成
* 【2022/12/18】[Config update page](#67-add-new-page) : app10を作成
* 【2022/12/18】[Config parser page](#67-add-new-page) : app11を作成
* 【2022/12/19】[Table preview page](#67-add-new-page) : app12を作成
* 【2022/12/19】[Visual page](#67-add-new-page) : app13を作成
## 3. Coming soon
- [ ] グラフ可視化方法の検討

## 4. Quick Start

### 4.1. ✨ Start the app in Docker

👉 **Step 1** - ソースコードをダウンロードします．

```bash
$ git clone https://github.com/HamaruKi0303/flask-black-dashboard.git
$ cd flask-black-dashboard
```

<br />

👉 **Step 2** - `Docker`を起動します．

```bash
$ docker-compose up --build 
```

`http://localhost::7777` にアクセスするとダッシュボードの画面が確認できます．

![](https://i.imgur.com/SsY476Z.png)


## 5. Detail



### 5.1. ✨ フォルダ構成


```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```



## 6. Sample basic site

機能別に簡易的なページの例を下記に記載します．

### 6.1. Simple text page

アクセスするとテキストを返すような一番簡易的なページです．

`apps\home\sample\app1.py`
```python
from flask import Blueprint

# Blueprint を作成
bp = Blueprint('sample_app1', __name__)

@bp.route('/sample_app1')
def sample_app1():
    return '!!  sample_app1  !!'
```


👇サイト
> URL: http://192.168.0.100:7777/sample_app1

![](https://i.imgur.com/TaaA7V1.png)

### 6.2. Simple HTML page


`HTML`を返すページです．こちらのファイル`sample/app2.html`を返すページです．Postの送受信機能はありません．

`apps\home\sample\app2.py`
```python
from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

# Blueprint を作成
bp = Blueprint('sample_app2', __name__)

@bp.route('/sample_app2')
def sample_app2():
    return render_template('sample/app2.html')
```

👇サイト
> http://192.168.0.100:7777/sample_app2

![](https://i.imgur.com/6MTEMEE.png)


### 6.3. POST page

POSTでやり取りをします．入力フォームのデータをCSVに保存し，テーブルで表示します．

`apps\home\sample\app3.py`

```python
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
    
    # データの保存 path
    form_data_path = "apps/static/assets/data/form_data.csv"
    df_form = pd.read_csv(form_data_path, index_col=0)
    
    # POSTメソッドの場合
    if request.method == 'POST':

        # Dict に変換
        dict_form = request.form.to_dict()
        # データフレームに追加
        df_form = df_form.append(dict_form, ignore_index=True)
        
        logger.info("df_form")
        # CSVで保存
        df_form.to_csv(form_data_path)
        pprint.pprint(df_form)
        
        logger.info("dict_list_form")
        # データフレームを Dict に変換
        dict_list_form = df_form.to_dict('records')
        pprint.pprint(dict_list_form)
        # name = request.form['name']
        
    return render_template('sample/app3.html', dict_list_form=dict_list_form)
```

👇サイト
> http://192.168.0.100:7777/sample_app3

![](https://i.imgur.com/3624YnZ.png)

### 6.4. Active sidebar

サイドバーにアクティブのマークを付けます．

`segment`でページのタイトルを送ります．

`apps\home\sample\app4.py`

```python
from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app4', __name__)

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app4', methods=['GET', 'POST'])
def sample_app4():
    
    segment = "sample_app4"
    
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
    
    return render_template('sample/app3.html', 
                            dict_list_form=dict_list_form, 
                            segment=segment)
```

送信した`segment`を`HTML`側で受け取ってアクティブにします．

`apps\templates\includes\sidebar.html`

```html

...

                <li class="{% if 'sample_app4' in segment %} active {% endif %}">
                    <a href="/sample_app4">
                        <i class="tim-icons icon-spaceship"></i>
                        <p>Sample4</p>
                    </a>
                </li>
...

```
👇サイト
> http://192.168.0.100:7777/sample_app4

![](https://i.imgur.com/DPA1UEF.png)


### 6.5. Switch sidebar

開発用と本番用でサイドバーを切り替えます．

`running_type`で開発用か本番用かのフラグを送ります．

`apps\home\sample\app5.py`

```python
from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

import pandas as pd
import pprint
from loguru import logger
# Blueprint を作成
bp = Blueprint('sample_app5', __name__)

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app5', methods=['GET', 'POST'])
def sample_app5():
    
    segment = "sample_app5"
    # running_type = "develop"
    running_type = "master"
    
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
    
    return render_template('sample/app3.html', 
                            dict_list_form=dict_list_form, 
                            segment=segment, 
                            running_type=running_type)
```

送信した`running_type`を受け取って，本番用なら特になにもしません．一方で開発用なら，`includes/sidebar_develop.html`を読み込みサイドバーを追加します．

`apps\templates\includes\sidebar.html`

```html

...

                <li class="{% if 'sample_app4' in segment %} active {% endif %}">
                    <a href="/sample_app4">
                        <i class="tim-icons icon-spaceship"></i>
                        <p>Sample4</p>
                    </a>
                </li>
                <li class="{% if 'sample_app5' in segment %} active {% endif %}">
                    <a href="/sample_app5">
                        <i class="tim-icons icon-spaceship"></i>
                        <p>Sample5</p>
                    </a>
                </li>
                
                {% if 'master' in running_type  %}

                {% else %}
                    {% include 'includes/sidebar_develop.html' %}                    
                {% endif %}

                <li>
                    <a href="{{ url_for('authentication_blueprint.logout') }}">
                        <i class="tim-icons icon-button-power"></i>
                        <p>Logout</p>
                    </a>
                </li>
...

```
👇サイト
> http://192.168.0.100:7777/sample_app5

![](https://i.imgur.com/6wIjjec.png)



### 6.6. Simple progress bar

シンプルな構成でプログレスバーを作成します．

処理している関数側で進捗状況を`Queue`に送信します．これをストリームが受け取ります．

`apps\home\sample\app6.py`

```python
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
```

進捗状況をストリームが受け取ると`Response`でサイトに返すと`addEventListener`によりプログレスバーが進捗状況に合わせて変更される仕組みです．

`apps\templates\sample\app6.html`

```html

...


                    <!-- POST フォーム -->
                    <form action="/sample_app6" method="post">
                        <!-- 処理開始ボタン -->
                        <div class="card-footer text-center">
                            <button type="submit" class="btn btn-fill btn-primary">Start processing</button>
                        </div>
                    </form>

                    <!-- プログレスバー表示エリア -->
                    <div class="progress_wrap bg-dark m-5">
                        <div class="progress-bar progress-bar-striped" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                            <span class="progress-bar-label mx-2">0%</span>
                        </div>
                    </div>

                    <!-- 結果表示エリア -->
                    <p id="result" class="text-center my-5">経過時間 : {{ dict_form['elapsed_time'] }}</p>




...

<!-- プログレスバーの値の受信 -->
<script>
    $(function(){
        var source = new EventSource("/stream");
        source.addEventListener('progress-item', function(event){
            $('.progress-bar').css('width', event.data + '%').attr('aria-valuenow', event.data);
            $('.progress-bar-label').text(event.data + '%');
        }, false);

        source.addEventListener('last-item', function(){
            source.close();
            $('.progress-bar').css('width', '100%').attr('aria-valuenow', 100);
            $('.progress-bar-label').text('100%');
        }, false);
     
    });
    </script>

...

```
👇サイト
> http://192.168.0.100:7777/sample_app6

![](https://i.imgur.com/062jQJQ.png)



### 6.7. Add new page

新しいページの追加方法です．


**Step1 : ファイルの作成**

`.py`と`.html`ファイルを作成しておきます．ここでは`app6`を例にして説明をします．

![](https://i.imgur.com/4Ls8nGr.png)

**Step2 : パスの追加**

下記のファイルに作成した`.py`ファイルと関連付けをします．
`apps\__init__.py`

```python
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

．．．


# ----------------------------------------
# my bp site 
#
from apps.home.sample.app1 import bp as sample_app1
from apps.home.sample.app2 import bp as sample_app2
from apps.home.sample.app3 import bp as sample_app3
from apps.home.sample.app4 import bp as sample_app4
from apps.home.sample.app5 import bp as sample_app5
from apps.home.sample.app6 import bp as sample_app6


．．．


def create_app(config):

    ．．．

    
    # regit sample site 
    app.register_blueprint(sample_app1)
    app.register_blueprint(sample_app2)
    app.register_blueprint(sample_app3)
    app.register_blueprint(sample_app4)
    app.register_blueprint(sample_app5)
    app.register_blueprint(sample_app6)
    
    configure_database(app)
    return app

```

**Step3 : サイドバーへの追加**


下記のファイルに`segment`の名前と`/sample_app6`を編集して完了です．

`apps\templates\includes\sidebar.html`


```html

...
                <li class="{% if 'sample_app6' in segment %} active {% endif %}">
                    <a href="/sample_app6">
                        <i class="tim-icons icon-spaceship"></i>
                        <p>Sample6</p>
                    </a>
                </li>
...

```


## 7. Sample chart site

入力フォームデータの保存からログデータの統合，データの簡単な可視化までをやっていきます．

### 7.1. Simple chart

シンプルなグラフを作成します．

![](https://i.imgur.com/ceFrV6c.png)

デフォルトのダッシュボードの関数を切り出してきて使用しています．

(*数値やラベルは`javascript`で直書きしています)



`.py`は`HTML`をただ返すだけのシンプルな構成です．

`apps\home\sample\app7.py`

```python

...

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/sample_app7', methods=['GET', 'POST'])
def sample_app7():
    
    segment = "sample_app7"
    # running_type = "develop"
    running_type = "master"
    
    return render_template('sample/app7.html', 
                            segment=segment, 
                            running_type=running_type)
```


`apps\templates\sample\app7.html`の`body`は特になにもしていません．ここで指定した`ID`(chartLinePurple, CountryChart)を下記のコードで使用します．


```html

...


        <!-- chartLinePurple  -->
        <div class="col-12">
            <div class="card card-chart">
                <div class="card-header">
                    <h5 class="card-category">Sample chart</h5>
                    <h2 class="card-title">ID : chartLinePurple</h2>
                </div>
                <div class="card-body">
                    <div class="chart-area">
                        <canvas id="chartLinePurple"></canvas>
                    </div>
                </div>
            </div>
        </div>
        <!-- CountryChart  -->
        <div class="col-12">
            <div class="card card-chart">
                <div class="card-header">
                    <h5 class="card-category">Sample bar</h5>
                    <h2 class="card-title">ID : CountryChart</h2>
                </div>
                <div class="card-body">
                    <div class="chart-area">
                        <canvas id="CountryChart"></canvas>
                    </div>
                </div>
            </div>
        </div>


...


```

下記のスクリプトを`apps\templates\sample\app7.html`に記載することでチャートが表示されます．



```html

...

<script>

$(document).ready(function () {
        // -----------------------------------------------------------
        // -------------   chartLinePurple   -------------------------
        // -----------------------------------------------------------

        gradientChartOptionsConfigurationWithTooltipPurple = {
        maintainAspectRatio: false,
        legend: {
            display: false
        },

        tooltips: {
            backgroundColor: '#f5f5f5',
            titleFontColor: '#333',
            bodyFontColor: '#666',
            bodySpacing: 4,
            xPadding: 12,
            mode: "nearest",
            intersect: 0,
            position: "nearest"
        },
        responsive: true,
        scales: {
            yAxes: [{
                barPercentage: 1.6,
                gridLines: {
                    drawBorder: false,
                    color: 'rgba(29,140,248,0.0)',
                    zeroLineColor: "transparent",
                },
                ticks: {
                    suggestedMin: 60,
                    suggestedMax: 125,
                    padding: 20,
                    fontColor: "#9a9a9a"
                }
            }],

            xAxes: [{
                barPercentage: 1.6,
                gridLines: {
                    drawBorder: false,
                    color: 'rgba(225,78,202,0.1)',
                    zeroLineColor: "transparent",
                },
                ticks: {
                    padding: 20,
                    fontColor: "#9a9a9a"
                }
            }]
        }
        };


        var ctx = document.getElementById("chartLinePurple").getContext("2d");

        var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

        gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
        gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
        gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors

        var data = {
        labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        datasets: [{
            label: "Data",
            fill: true,
            backgroundColor: gradientStroke,
            borderColor: '#d048b6',
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: '#d048b6',
            pointBorderColor: 'rgba(255,255,255,0)',
            pointHoverBackgroundColor: '#d048b6',
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: [80, 100, 70, 80, 120, 80],
        }]
        };

        var myChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: gradientChartOptionsConfigurationWithTooltipPurple
        });

        // -----------------------------------------------------------
        // -------------   CountryChart   ----------------------------
        // -----------------------------------------------------------

        gradientBarChartConfiguration = {
        maintainAspectRatio: false,
        legend: {
            display: false
        },

        tooltips: {
            backgroundColor: '#f5f5f5',
            titleFontColor: '#333',
            bodyFontColor: '#666',
            bodySpacing: 4,
            xPadding: 12,
            mode: "nearest",
            intersect: 0,
            position: "nearest"
        },
        responsive: true,
        scales: {
            yAxes: [{

            gridLines: {
                drawBorder: false,
                color: 'rgba(29,140,248,0.1)',
                zeroLineColor: "transparent",
            },
            ticks: {
                suggestedMin: 60,
                suggestedMax: 120,
                padding: 20,
                fontColor: "#9e9e9e"
            }
            }],

            xAxes: [{

            gridLines: {
                drawBorder: false,
                color: 'rgba(29,140,248,0.1)',
                zeroLineColor: "transparent",
            },
            ticks: {
                padding: 20,
                fontColor: "#9e9e9e"
            }
            }]
        }
        };


        var ctx = document.getElementById("CountryChart").getContext("2d");

        var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

        gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
        gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
        gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors


        var myChart = new Chart(ctx, {
        type: 'bar',
        responsive: true,
        legend: {
            display: false
        },
        data: {
            labels: ['USA', 'GER', 'AUS', 'UK', 'RO', 'BR'],
            datasets: [{
            label: "Countries",
            fill: true,
            backgroundColor: gradientStroke,
            hoverBackgroundColor: gradientStroke,
            borderColor: '#1f8ef1',
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [53, 20, 10, 80, 100, 45],
            }]
        },
        options: gradientBarChartConfiguration
        });


    });

</script>

...

```

👇サイト
> http://192.168.0.100:7777/sample_app7

### 7.2. Radio & Date form page

ラジオボタンで項目を選択し，登録する日付を選択するフォームを作成します．

![](https://i.imgur.com/rmefyJb.png)

ラジオボタン部分は`apps\templates\sample\app8.html`の下記の部分です．

`data-toggle="buttons"`を忘れるとまともに機能しないので注意です．後は，通常のフォームとやることは変わりません．

```html
    <div class="btn-group btn-group-toggle" data-toggle="buttons">
        {% for j in range(1,dict["step-num"]+dict["step-num2"]) %}
        <label class="btn btn-sm btn-primary btn-simple"
            id={{dict["name"]}}_{{i+1}}_{{j+1}}>
            <input type="radio" name={{dict["name"]}}_{{i+1}}
                id={{dict["name"]}}_{{i+1}}_{{j+1}} autocomplete="off"
                value={{dict[j|string]}}>
            {{dict[j|string]}}
        </label>
        {% endfor %}
    </div>
```

日付の部分はこちらです．

```html
    <label class="label2" for="logging-time">
        <input class="input2" type="datetime-local" id="logging-time"
            name="logging-time" value={{dict["tstr-value"]}}>
    </label>
```

これを追加することで，日付を選択することができます．

![](https://i.imgur.com/ObJfsy4.png)

`label2`, `input2`のデザインはこちらです．

`apps\static\assets\demo\demo.css`
```css
    .label2 {
        position: relative;
        display: inline-block;
        width: 200px;
        height: 36px;
        border: 2px solid #ccc;
        border-radius: 15px;
    }
    .input2 {
        position: relative;
        padding: 0 10px;
        width: 200px;
        height: 36px;
        border: 0;
        background: transparent;
        box-sizing: border-box;
        font-size: 14px;
        color: #999;
    }
```

### 7.3. Index page

ページが長くなるとショートカットが欲しくなります．そこで，目次を作成してそこにショートカットを貼ることで一瞬で該当箇所に飛べるようにしました．

![](https://i.imgur.com/PRLjwGo.png)

各カードに`ID`を指定しておきます．
```html
    <div class="card-body" id={{dict["name"]}}>
        <div class="table-responsive">
```

あとは，これに飛ぶように指定することでショートカットが作成できます．
```html
    <td>
        <a href=#{{dict["name"]}}>{{dict["name"]}}</a>
    </td>
```


### 7.4. Config update page

`Config`ファイル(`apps\static\assets\data\category_weight.csv`)をアプリから修正できるようにしました．

![](https://i.imgur.com/Uzi93F9.png)


### 7.5. Config parser page

アプリのログファイルの場所やデータの保存場所などの設定を記載する`INI`ファイル(`apps\static\assets\config\example_config.ini`)を使用できるようにしました．

`apps\home\sample\app11.py`
```python
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
```




### 7.6. Table preview page

`DataFrame`をHTMLのテーブルで表示できるようにしました．


![](https://i.imgur.com/helghNO.png)



HTMLでループ処理しやすいように`to_dict('records')`で変換します．

`apps\home\sample\app12.py`
```python
    dict_list_form = df_weight_total.to_dict('records')

    return render_template(render_template_path,
                           segment=segment,
                           dict_list_form=dict_list_form,
                           running_type=running_type)
```

変換後は`dict_list_form`に渡され，ループ処理をすることで各列の情報を記載していきます．
`apps\templates\sample\app12.html`
```html
    <div class="card-body">
        <div class="table-responsive">
            <table class="table tablesorter " id="">
                <thead class=" text-primary">
                    <tr>
                        <th>
                            Date
                        </th>
                        <th>
                            Name
                        </th>

                    </tr>
                </thead>
                <tbody>
                    {% for dict in dict_list_form %}
                    <tr>
                        <td>
                            {{dict["tstr-min"]}}
                        </td>
                        <td>
                            {{dict["weight_name"]}}
                        </td>
                        {% for i in range(1, 16) %}
                        <td>
                            {{dict[i|string]}}
                        </td>
                        {% endfor %}
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
```

### 7.7. Visual page

`DataFrame`を使ってグラフに可視化していきます．

![](https://i.imgur.com/XfTLae5.png)

チャート用の辞書(`chart_dcit`)を用意します．ここで`x`,`y`に数値を入れることで描画できます．
`apps\home\sample\app13.py`

```python
    chart_dcit = {}
    target_weight_name = "Abdominal-Crunch"
    target_df_merged_data = df_merged_data[df_merged_data["weight_name"] == target_weight_name]
    logger.info("target_df_merged_data : \n{}".format(target_df_merged_data))
    target_df_merged_data = target_df_merged_data.drop(['ID', 'tstr-min', 'tstr-day', 'weight_name', 'total'], axis=1)
    logger.info("target_df_merged_data : \n{}".format(target_df_merged_data))
    chart_dcit[target_weight_name] = {}
    chart_dcit[target_weight_name]["x"] = list(range(len(target_df_merged_data.values.reshape(-1))))
    chart_dcit[target_weight_name]["y"] = list(target_df_merged_data.values.reshape(-1))
```

HTML内のjavascriptはこんな感じです．
`apps\templates\sample\app13.html`
```js
        var data = {
        labels: {{chart_dcit["Abdominal-Crunch"]["x"]}},
        datasets: [{
            label: "Data",
            fill: true,
            backgroundColor: gradientStroke,
            borderColor: '#d048b6',
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: '#d048b6',
            pointBorderColor: 'rgba(255,255,255,0)',
            pointHoverBackgroundColor: '#d048b6',
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: {{chart_dcit["Abdominal-Crunch"]["y"]}},
        }]
        };
```


## 8. Reference site

- [flask-black-dashboard](https://github.com/app-generator/flask-black-dashboard)
- [Flaskで簡易版プログレスバー実装して処理の進捗見れるようにしてやんよ!!!](https://tokidoki-web.com/2020/02/flask%E3%81%A7%E7%B0%A1%E6%98%93%E7%89%88%E3%83%97%E3%83%AD%E3%82%B0%E3%83%AC%E3%82%B9%E3%83%90%E3%83%BC%E5%AE%9F%E8%A3%85%E3%81%97%E3%81%A6%E5%87%A6%E7%90%86%E3%81%AE%E9%80%B2%E6%8D%97%E8%A6%8B/)
- [html･CSS ラジオボタンを横並びや縦並びにする方法](https://csshtml.work/side-radio/)
- [HTML5の日付入力フォームのスタイルを変えてみる](https://blog.mmmcorp.co.jp/blog/2016/10/20/input_date_style/)
## 9. memo

```bash
rsync -auv /home/ /root/
python run.py
```
