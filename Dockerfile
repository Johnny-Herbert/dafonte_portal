FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
COPY requirements.txt /app/

RUN apk update && apk add bash postgresql-dev gcc python3-dev musl-dev
RUN apk add build-base py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install psycopg2

RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000

ADD . /app/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
