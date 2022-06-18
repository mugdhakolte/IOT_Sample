FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip

COPY docs/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY .env /code/.env