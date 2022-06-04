FROM python:latest

WORKDIR /app/
COPY ./ /app


# prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1


RUN pip3 install -r /app/requirements.txt
ENV PYTHONPATH=/app