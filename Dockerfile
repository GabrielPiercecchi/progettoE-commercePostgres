# pull official base image
FROM python:3.10-slim-buster

# create directory fot the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app


# Next, we will move forward and create our app directory where we will copy our code.
ENV HOME=/home/app
ENV APP_HOME=/home/app/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -U setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# After that I will copy the entire code, change ownership and finally run the gunicorn process at port 5000.
# add app
COPY . .

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run gunicorn
CMD gunicorn --bind 0.0.0.0:5000 main:app -k uvicorn.workers.UvicornWorker



