FROM ubuntu
RUN apt-get update
RUN apt-get install python3
RUN apt-get install python3-pip

COPY . /app
WORKDIR app/
RUN pip install -r requirements.txt
