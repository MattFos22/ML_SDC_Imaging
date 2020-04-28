FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /ML-SGD
WORKDIR /ML-SGD
ADD . /ML-SGD/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn web_project.wsgi:application — bind 0.0.0.0:8000 — workers 3
