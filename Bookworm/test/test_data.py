import pytest
import pandas as pd

from data.database import MongoDB,Redis


sample_data =  pd.DataFrame([['apple', 'fruit'],
                        ['milk', 'drink'], ['pizza', 'food']], 
                        columns=['object', 'type'])


def test_mongo(sample_data=sample_data):
    sample_dict = sample_data.to_dict('records')
    database = MongoDB()
    database.store(sample_dict, 'test', 'test_table')
    res = database.load('test', 'test_table', columns=sample_data.columns)
    
    assert type(res) == type(sample_data)

def test_redis(sample_data=sample_data):
    sample_json = sample_data.to_json(orient='records')
    database = Redis()
    database.store(sample_json, 'test', 1)
    res = database.load('test', 1)
    assert type(res) == list
