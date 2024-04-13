FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt-get install -y antiword
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]