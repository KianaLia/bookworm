from pymongo import MongoClient
import redis 
import pandas as pd
import json
import io
import re

#Parent class
class Database():
  def __init__(self):
    pass

  def store(self, **kwargs):
    pass

  def load(self, **kwargs):
    pass

#Child classes
class MongoDB(Database):
  def store(self, data, db_name:str, table_name:str):
    if not isinstance(data, list):
      raise Exception('you must insert a dict to store!')
    client = MongoClient('mongodb://mongo:27017/')
    database = client[db_name]
    collection = database[table_name]

    result = collection.insert_many(data)
    total_docs = len(result.inserted_ids)
    print(
        f'Data inserted into \n {table_name} table in MongoDB \n total docs inserted: {total_docs}'
    )

  def load(self, db_name:str, table_name:str, columns):
    client = MongoClient('mongodb://mongo:27017/')
    database = client[db_name]
    collection = database[table_name]
    df_table = pd.DataFrame(list(collection.find()), columns=columns)
    print(f'{table_name} Table Loaded from Mongo')

    return df_table

class Redis(Database):
  def store(self, data, key:str, id):
    if key is None:
      raise Exception('you MUST insert a key to store!')
    elif not isinstance(data, str):
        raise Exception('you must insert a json-like to store!')
    else:
      redis_client = redis.StrictRedis(host='redis', db=0)
      redis_client.set(f'{key}{id}', data)

      print(f"{key}{id} Data Is stored in redis!")

  def load(self, key:str, id):
    redis_client = redis.StrictRedis(host='redis', db=0)
    data = redis_client.get(f'{key}{id}').replace(b'\'', b'\"')
    return json.load(io.BytesIO(data))
