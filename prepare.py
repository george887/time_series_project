
# Creating is in ds column
df['is_ds'] = df.cohort_id.isin([30,34,55,59])

# Creating a mask for users accessing pages after graduation
after_grad = df[df.accessed_while_enrolled == False]

