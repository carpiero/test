if __name__ == '__main__':
    import pandas as pd
    data = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/Arrests.csv',# dataset about Arrests for Marijuana Possession
    index_col=0)
    print(type(data))
    def get_means(df):

        numeric = df._get_numeric_data()
        means_df = pd.DataFrame(numeric.mean()).reset_index()
        means_df.columns = ['colname', 'mean']
        return means_df

    print(get_means(data))