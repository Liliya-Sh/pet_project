FROM python:3.12-alpine

RUN apk add --no-cache postgresql-dev gcc musl-dev

WORKDIR /pet_project

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt

COPY ./restaurant_ordering_system /pet_project/restaurant_ordering_system
COPY ./run.sh .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN chmod +x /run.sh
CMD ["sh","/run.sh"]
