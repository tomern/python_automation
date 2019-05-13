FROM python:latest
COPY . /app
WORKDIR app
RUN pip install --upgrade pip
RUN pip install docker-py feedparser nosexcover prometheus_client pycobertura pylint pytest pytest-cov requests setuptools sphinx pytest-html pytest-xdist
RUN pip install -r requirements.txt

