FROM python:latest

RUN mkdir /test
WORKDIR /test
COPY test /test
RUN pip install --no-cache-dir -r requirements.txt
# CMD [ "python", "-m pytest" ]
CMD ["pytest"]
