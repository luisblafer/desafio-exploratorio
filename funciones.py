import pandas as pd

def missing_zero_values_table(df):
    zero_values = (df == 0.00).astype(int).sum(axis=0)
    missing_values = df.isnull().sum()
    missing_values_percent = 100 * df.isnull().sum() / len(df)
    mz_table = pd.concat([zero_values, missing_values, missing_values_percent], axis=1)
    mz_table = mz_table.rename(
        columns = {0: 'Zero Values', \
                   1: 'Missing Values', \
                   2: '% of Total Values'})
    mz_table['Total Zero Missing Values'] = mz_table['Zero Values'] + \
        mz_table['Missing Values']
    mz_table['% Total Zero Missing Values'] = 100 * \
        mz_table['Total Zero Missing Values'] / len(df)
    mz_table['Data Type'] = df.dtypes
    mz_table = mz_table[
        mz_table.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(2)
    print(f"Your selected dataframe has {df.shape[1]} columns and {df.shape[0]} Rows.\n"
          f"There are {mz_table.shape[0]} columns that have missing values.")
#         mz_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
    return mz_table
