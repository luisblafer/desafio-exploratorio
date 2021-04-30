import pandas as pd
import numpy as np

def missing_zero_values_table(df):
    zero_values = (df == 0.00).astype(int).sum(axis=0)
    missing_values = df.isnull().sum()
    missing_values_percent = df.isnull().sum() / len(df)
    mz_table = pd.concat([zero_values, missing_values, missing_values_percent], axis=1)
    mz_table = mz_table.rename(
        columns = {0: 'Zero Values', \
                   1: 'Missing Values', \
                   2: '% of Total Values'})
    mz_table['Total Zero Missing Values'] = mz_table['Zero Values'] + \
        mz_table['Missing Values']
    mz_table['% Total Zero Missing Values'] = \
        mz_table['Total Zero Missing Values'] / len(df)
    mz_table['Data Type'] = df.dtypes
    mz_table = mz_table[
        mz_table.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False)
    print(f"Your selected dataframe has {df.shape[1]} columns and {df.shape[0]} Rows.\n"
          f"There are {mz_table.shape[0]} columns that have missing values.")
#         mz_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
    mz_table = mz_table.style.format({'% of Total Values': "{:.2%}", '% Total Zero Missing Values': '{:.2%}'})
    return mz_table

def remover_ppm2_outliers(df):
    '''
    Returns a dataframe without outliers up to 2 deviations away from the std

            Parameters:
                    df (DataFrame): Input DataFrame with potential outliers

            Returns:
                    df_out (pd.DataFrame): DataFrame without the outliers
    '''
    df_out = pd.DataFrame()
    for key, subdf in df.groupby("place_name"):
        m = np.mean(subdf.price_per_m2_covered_clean)
        st = np.std(subdf.price_per_m2_covered_clean)*2
        reduced_df = subdf[(subdf.price_per_m2_covered_clean>(m-st)) & (subdf.price_per_m2_covered_clean<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
