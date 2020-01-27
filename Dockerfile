FROM python:3.8

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

# RUN docker run --rm -it -p 5432:5432 postgres:10
# RUN python init_db.py
