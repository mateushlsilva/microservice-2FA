FROM python:alpine

WORKDIR /usr/src/app

COPY ./ /usr/src/app/

RUN pip install Flask pymongo twilio
RUN pip install python-dotenv

EXPOSE 5000

CMD [ "python", "app.py" ]