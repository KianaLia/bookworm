import pandas as pd
import numpy as np
from scipy.sparse import csr, csr_matrix
from sklearn.neighbors import NearestNeighbors
import json
from datetime import datetime

from data.database import *


#Parent class
class Model():
  def __init__(self, name, data_tag, hyper_params=None, params=None):
    self.name = name
    self.data_tag = data_tag
    self.hyper_params = hyper_params
    self.params = params
    
  def info(self, general_info):
    model_info = {"General" : general_info,
                "Hyper_params" : self.hyper_params,
                "Params" : self.params}
    json_info = json.dumps(model_info)

    return json_info

  def run(self):
    pass

class KNN(Model):
  def __init__(self, name, data, data_tag, hyper_params=None, params=None):
    Model.__init__(self, name, data_tag, hyper_params=None, params=None)
    self.data = data

  def run(self, user_id, n_recommend):

    if not ( user_id in (self.data['AccountId'].tolist()) ):
      print('User {} has no Action Data!'.format(user_id))
      return []
    else:
      #preprocess + tarining knn model
      def csr_matrix_maker(df):
          ones = np.ones(df.shape[0])
          df['read'] = ones
          df.read = df.read.astype(dtype='int32')
          csr_data = csr_matrix(
              (df.read.values, (df.BookId.values, df.AccountId.values)))

          return df, csr_data
      self.data, csr_data = csr_matrix_maker(self.data)

      knn_model = NearestNeighbors(metric='cosine',
                                  algorithm='brute',
                                  n_neighbors=14,
                                  n_jobs=-1)
      knn_model.fit(csr_data)

      #Finding book that the user has reacted to
      book_id_list = []
      for item in (self.data[self.data['AccountId'] == user_id]).values:
          book_id_list.append(item[1])

      #Getting recommendations based on actions of the user
      act_recom = []

      for book in book_id_list:
          distances, indices = knn_model.kneighbors(csr_data[book],
                                                  n_neighbors=n_recommend + 1)
          recom = sorted(list(
              zip(indices.squeeze().tolist(),
                  distances.squeeze().tolist())),
                      key=lambda x: x[1])[1:]
          act_recom += recom

      #Storeing Model infromation in redis 
      self.params = {}
      self.hyper_params = knn_model.get_params()
      time = datetime.today().strftime('%Y-%m-%d')
      general_info = {'date' : time, 'name': type(knn_model).__name__}
      json_info = self.info(general_info)

      database = Redis()
      database.store(json_info, self.data_tag, user_id)

      return act_recom


