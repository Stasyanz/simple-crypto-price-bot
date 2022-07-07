FROM python:3.9
LABEL maintainer="stasyanzayac@gmail.com"

WORKDIR /app/
ADD . /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python", "-u", "src/main.py"]