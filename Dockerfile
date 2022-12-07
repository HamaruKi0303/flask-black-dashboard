FROM python:3.9

WORKDIR /flask_base

# init
RUN apt-get update && \
    apt-get install -y rsync

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP run.py
ENV DEBUG True

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY env.sample .env

COPY . .

# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade

# install pip utils
RUN pip install loguru \
                pandas

# gunicorn
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
# gunicorn --config gunicorn-cfg.py run:app