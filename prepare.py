
import pandas as pd

###################### Preparing data ##################
def prep_data(df):
    # Creating is in ds column
    df['is_ds'] = df.cohort_id.isin([30,34,55,59])

    #creating a columns accessed
    df['times_accessed'] = 1

    # Dropping all request to the home page and table of contents
    df = df[df.page != '/']
    df = df[df.page != 'toc']
    df = df[df.cohort_id != 28]
    df = df[df.page != 'search/search_index.json']

    # Loading the cohort csv to add to original df
    cohort_df = pd.read_csv('cohorts.csv')

    # Creating a date column
    df['date'] = df.index

    # Merging the original data frame with cohort_df
    df = df.merge(cohort_df, on ='cohort_id', how = 'left')

    # Reseting the index
    df.index = df.date

    # Changing the start and end date to datetime format
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)

    # Mask for looking at pages while enrolled
    df['accessed_while_enrolled'] = ((df.date >= df.start_date) & (df.date <= df.end_date))

    return df

#################### Creating ds data frame for accessing curriculum ##########################
def ds_pgs_accessed(df):
    # Sorting by times accessed
    df = df.sort_values(by = 'times_accessed', ascending=False)
    # Selecting only ds students
    df = df[df.is_ds == True]
    return df

#################### Creating webdev data frame for accessing curriculum ##########################
def wd_pgs_accessed(df):
    # Sorting by times accessed
    df.sort_values(by = 'times_accessed', ascending=False)
    # Selecting only ds students
    df = df[df.is_ds == False]
    return df

##################### Creating only DS data set for looking at pages after graduating ###################

# Creating a mask for users accessing pages after graduation
def ds_after_grad_data(df):
    
    # mask for ds students after graduating
    ds_after_grad = df[df.accessed_while_enrolled == False]

    # mask for only ds students
    ds_after_grad = df[df.is_ds == True]

    return ds_after_grad

##################### Creating only web dev data set for looking at pages after graduating ###################
def wd_after_grad_data(df):
    # mask for ds students after graduating
    wd_after_grad = df[df.accessed_while_enrolled == False]

    # mask for only ds students
    wd_after_grad = df[df.is_ds == False]

    return wd_after_grad




