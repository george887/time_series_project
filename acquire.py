import pandas as pd

def get_curric_data():
    '''
    This function takes in the curriculum csv, cleans up the columns, and sets the time stamp as the index
    '''
    # Getting the csv
    df = pd.read_csv('anonymized-curriculum-access.txt', sep=" ", header=None)
    # Creating a time_stamp column
    df['time_stamp'] = df[0] + ' ' + df[1]
    # Dropping un wanted columns
    df = df.drop(columns = [0,1])
    # Renaming columns to read easier
    df = df.rename(columns={2: "page", 3:'user_id', 4:'cohort_id', 5:'ip'})
    # Time_stamp to date time
    df.time_stamp = pd.to_datetime(df.time_stamp)
    # Setting the index
    df = df.set_index('time_stamp')
    return df