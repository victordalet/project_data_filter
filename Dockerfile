FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN export PYTHONPATH=$(pwd)/src:$(pwd)
CMD python3 src/main.py