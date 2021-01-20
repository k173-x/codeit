FROM python:3.7

WORKDIR /code

RUN pip install setuptools

COPY . .

RUN pip install .

CMD ["codeit"]
