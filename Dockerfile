
FROM python:3.9-alpine
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -U kafka-python
RUN pip install -U flask


COPY . /app
ENTRYPOINT ["python", "main.py"]
