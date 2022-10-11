import pandas as pd
import pytest

from model.model import *

def test_knn():
    database = MongoDB()
    actions = database.load('actions', 'actions_table', ['AccountId', 'BookId'] )
    sample_uid = 20163
    n_recommend = 5

    model = KNN('KNN', data_tag='actions', data=actions)
    res = model.run(sample_uid, n_recommend)
    act = [ rec[0] for rec in res ]
    final_recom = act[:n_recommend]
    
    assert isinstance(final_recom, list)
    assert all(isinstance(x, int) for x in final_recom)