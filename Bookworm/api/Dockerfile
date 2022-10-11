FROM python:latest

RUN mkdir /api
WORKDIR /api
COPY api /api
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]
