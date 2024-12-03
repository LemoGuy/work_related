import pandas as pd

# Load data
df = pd.read_csv('ABORI.csv')

# Debug column names
print("Columns in dataset:", df.columns)

# Choose the correct column to process
if 'Kurdish' in df.columns:
    # Split the Kurdish column into two parts: primary_word and synonyms
    df[['primary_word', 'synonyms']] = df['Kurdish'].str.split(',', n=1, expand=True)
    # Save cleaned data
    df.to_csv('ABORI_cleaned.csv', index=False)
    print("Data processed and saved to 'ABORI_cleaned.csv'")
else:
    print("Column 'Kurdish' not found in the dataset.")
