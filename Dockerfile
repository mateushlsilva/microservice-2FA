FROM python:alpine

WORKDIR /usr/src/app

COPY ./ /usr/src/app/

ENV email=${{ secrets.EMAIL }}
ENV senha=${{ secrets.EMAIL_PASS }}
ENV TWILIO_ACCOUNT_SID=${{ secrets.TWILIO_ACCOUNT_SID }}
ENV TWILIO_AUTH_TOKEN=${{ secrets.TWILIO_AUTH_TOKEN }}
ENV NUMBER=${{ secrets.NUMBER }}

RUN pip install Flask pymongo twilio
RUN pip install python-dotenv

EXPOSE 5000

CMD [ "python", "app.py" ]
