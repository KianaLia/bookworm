FROM python:latest

RUN mkdir /data
WORKDIR /data
COPY data /data
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "main.py" ]
