import pandas as pd 
df=pd.read_csv('survey_results_public.csv')
print(df.head())  # Display the first few rows of the DataFrame
print(df.info())  # Get a concise summary of the DataFrame
print(df.describe())  # Get descriptive statistics for numerical columns
print(df.shape)  # Get the shape of the DataFrame
pd.set_option('display.max_columns', 85)  # Set display option to show more columns
pd.set_option('display.max_rows', 85)  # Set display option to show more rows

schema_df=pd.read_csv('survey_results_schema.csv')
print(schema_df.head())  # Display the first few rows of the schema DataFrame
print(schema_df.info())  # Get a concise summary of the schema DataFrame
print(schema_df.describe())  # Get descriptive statistics for numerical columns in the schema