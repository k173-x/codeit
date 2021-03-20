FROM python:3.7

WORKDIR /code

RUN pip install setuptools

RUN pip install cxit

CMD ["codeit"]
