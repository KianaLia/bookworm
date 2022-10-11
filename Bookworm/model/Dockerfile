FROM python:latest

RUN mkdir /model
WORKDIR /model
COPY model /model
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]
