
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
- [6. Sample site](#6-sample-site)
  - [6.1. Simple text page](#61-simple-text-page)
  - [6.2. Simple HTML page](#62-simple-html-page)
  - [6.3. POST page](#63-post-page)
  - [6.4. Active sidebar](#64-active-sidebar)
  - [6.5. Switch sidebar](#65-switch-sidebar)
- [7. Reference site](#7-reference-site)
- [8. memo](#8-memo)

## 1. Introduction

`FLASK`製のダッシュボードのテンプレートです．


## 2. Updates!!
* 【2022/12/05】[元のサイト](https://github.com/app-generator/flask-black-dashboard)のフォーク & base `README.md` の追加
* 【2022/12/07】[サンプルサイト](#6-sample-site)：app1~app5を作成

## 3. Coming soon
- [ ] BPサンプルサイトの追加

## 4. Quick Start

### 4.1. ✨ Start the app in Docker

> 👉 **Step 1** - ソースコードをダウンロードします．

```bash
$ git clone https://github.com/app-generator/flask-black-dashboard.git
$ cd flask-black-dashboard
```

<br />

> 👉 **Step 2** - `Docker`を起動します．

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



## 6. Sample site

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

## 7. Reference site

- [flask-black-dashboard](https://github.com/app-generator/flask-black-dashboard)

## 8. memo

```bash
rsync -auv /home/ /root/
python run.py
```