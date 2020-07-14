FROM python:3.6-alpine
RUN apk add mysql-client \
    util-linux
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
