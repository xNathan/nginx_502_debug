FROM python:3.6

RUN pip install tornado --index-url=https://mirrors.aliyun.com/pypi/simple

WORKDIR /usr/local/app
COPY app.py .

CMD ["python", "-u", "app.py"]
