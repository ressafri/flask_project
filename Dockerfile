FROM python:3.6.5-slim

RUN mkdir /app

WORKDIR /app

ADD requirement.txt .

RUN pip install -r requirement.txt

ADD . .

EXPOSE 80


CMD ["gunicorn", "flask_blog:app", "-b", "0.0.0.0:80", "--workers", "4", "--reload"]
