FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    swig \
    libssl-dev \
    dpkg-dev \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
COPY requirements_dev.txt /code/
RUN pip install -U pip && pip install -Ur /code/requirements.txt && pip install -Ur /code/requirements_dev.txt

WORKDIR /code
COPY . /code/
RUN /code/manage.py collectstatic --noinput
