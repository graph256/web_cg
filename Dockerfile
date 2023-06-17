FROM python:3.11
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR .
RUN apt update && pip install --upgrade pip && mkdir "app"
RUN sudo apt install git && sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin;
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . .
