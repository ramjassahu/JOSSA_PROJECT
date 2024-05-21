import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [1, 1, 2, 2, 3],
    'C': ['a', 'b', 'c', 'c', 'c']
}

df = pd.DataFrame(data)

# Function to extract number of unique occurrences in each column
def count_unique(df):
    unique_counts = {}
    for column in df.columns:
        unique_counts[column] = df[column].nunique()
    return unique_counts

print(count_unique(df))
