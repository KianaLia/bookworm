import pandas as pd
from database import *

def main():

    data_path = ''
    
    #loading and cleaning Actions data
    actions = pd.read_csv(data_path + 'actions.csv')
    actions = actions.iloc[:1000]
    action_data = actions.to_dict('records')

    database = MongoDB()
    database.store(action_data, 'actions', 'actions_table')

if __name__ == '__main__':
    main()