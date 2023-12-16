import pandas as pd

# Load data from Excel files into two dataframes
file1_path = 'Book1.xlsx'
file2_path = 'Book2.xlsx'

df_day1 = pd.read_excel(file1_path)
df_day2 = pd.read_excel(file2_path)

# a. Perform merging to find names of students who attended the workshop on both days

common_names = pd.merge(df_day1, df_day2, on='Name', how='inner')['Name']
print("a. Names of students who attended the workshop on both days:")
print(common_names)

# b. Find names of all students who attended the workshop on either of the days

all_names = pd.merge(df_day1, df_day2, on='Name', how='outer')['Name']
print("\nb. Names of all students who attended the workshop on either of the days:")
print(all_names)

# c. Merge two data frames row-wise and find the total number of records

merged_df = pd.concat([df_day1, df_day2], ignore_index=True)
total_records = len(merged_df)
print("\nc. Total number of records in the merged data frame:", total_records)

# d. Merge two data frames and use two columns 'Name' and 'Duration' as multi-row indexes.

# Generate descriptive statistics for this multi-index.
merged_multiindex_df = pd.merge(df_day1, df_day2, on=['Name', 'Duration'],how='outer')
statistics_multiindex = merged_multiindex_df.groupby(['Name', 'Duration']).describe()
print("\nd. Descriptive statistics for the multi-index (Name, Duration):")
print(statistics_multiindex)