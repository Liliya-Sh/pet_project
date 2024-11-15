FROM python:3.12-alpine

WORKDIR /pet_project

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt

COPY ./pet_project .
COPY ./run.sh .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

CMD ["sh","run.sh"]