FROM python:3.10.6-buster
#  base image

WORKDIR /dummyproject
# set working directory, create if not exists

COPY requirements.txt requirements.txt
# copy requirements file to working directory
RUN pip install -r requirements.txt
# install requirements

COPY awesomeapp awesomeapp
# copy backend directory to working directory
COPY setup.py setup.py
# copy setup file to working directory
RUN pip install .
# install package

CMD uvicorn awesomeapp.simpleapi:api  --host 0.0.0.0 --port $PORT
# run the API
