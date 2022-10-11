import pandas as pd
from model import *
from data.database import *



def active_users(data):
    
    data['Activity'] = data.groupby('AccountId')['AccountId'].transform('count')
    active_users = data[data['Activity']>5]['AccountId'].tolist()

    return active_users

def main():
    #-----------------------initialization-------------------------
    #Loading Data
    database = MongoDB()
    actions = database.load('actions', 'actions_table', ['AccountId', 'BookId'] )

    #Model Initialization
    act_model = KNN('KNN', data_tag='actions', data=actions)

    #Number of recommendations and selecting active users to run the model for them
    num_recommendations = 5
    user_id_list = active_users(actions)[:5]
    #--------------------------------------------------------------

    #Running model on desired users
    for user_id in user_id_list:

        #Getting recomendations from actions
        print(user_id)

        #Book_recommendations based on Users actions
        act_recom = act_model.run(user_id, num_recommendations)

        #Turning the recommendations to jsonformat to store them in Redis
        act = [ rec[0] for rec in act_recom ]
        final_recom = act[:num_recommendations]

        result = [[user_id, 'KNN', 'actions', final_recom]]
        final_recom = pd.DataFrame(
            result,
            columns=['AccountId', 'Model', 'Data', 'Recommended_book_ids'],
            index=[0])

        json_recom = final_recom.to_json(orient='records')

        database = Redis()
        database.store(json_recom, 'user', user_id)


if __name__ == '__main__':
    main()