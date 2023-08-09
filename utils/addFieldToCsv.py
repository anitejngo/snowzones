import pandas as pd

# Define the data types for each column
dtypes = {'zipcode': str, 'city': str, 'dc': str}

# Read the CSV file into a pandas DataFrame with specified data types
data = pd.read_csv('../data/_zipcode_city_dc_snowload.csv', dtype=dtypes)

# Add a new column "snowload" with empty values
data['comment'] = ''
data['note'] = ''

# Write the updated data to a new CSV file
data.to_csv('_zipcode_city_dc_snowload.csv', index=False)