import numpy as np
import pandas as pd


from sklearn.metrics.pairwise import cosine_similarity


def cf_recommender(df: pd.DataFrame, search: str,):
    """
    Check if connected to git SVN
    """
    dfbooks_rating = df.copy()
    dfbooks_rating_count = dfbooks_rating.groupby('User-ID')\
                           .agg(['count'])['Book-Rating'].reset_index()
    # Count value more than 5
    xdfbooks_rating_userID = dfbooks_rating_count\
                             [dfbooks_rating_count['count'] > 5]

    # Filteing the required User of Dataset (Count more than 5 )
    xdfbooks_rating = dfbooks_rating[dfbooks_rating['User-ID']\
                      .isin(xdfbooks_rating_userID['User-ID'].tolist())]

    print("Shape: ", xdfbooks_rating.shape)
    # xdfbooks_rating.head()

    xdfbooks_count = xdfbooks_rating.groupby('Book-Title')\
                     .agg(['count'])['Book-Rating'].reset_index()
    xdfbooks_popular = xdfbooks_count[xdfbooks_count['count'] >= 5]
    xdfbooks_famous = xdfbooks_rating[xdfbooks_rating['Book-Title']\
                      .isin(xdfbooks_popular['Book-Title'].tolist())]\
                      .drop_duplicates()

    print("Shape: ", xdfbooks_famous.shape)
    # xdfbooks_famous.head()
    
    xdf_pivot = xdfbooks_famous.pivot_table(index='Book-Title',
                                            columns='User-ID',
                                            values='Book-Rating',)
    # xdf_pivot.head()
    print(f'xdf_pivot size: {xdf_pivot.shape}')
    xdf_pivot.fillna(0, inplace=True)
    # xdf_pivot.head()

    similarity_score = cosine_similarity(xdf_pivot)
    print("similarity_score size: ", similarity_score.shape)
    # similarity_score
    
    # Test functioning
    # np.where(xdf_pivot.index == 'Zoya')[0][0]
    
    # Verify the First Record of Similarity Score
    # sorted(list(enumerate(similarity_score[0])), key=lambda x:x[1], reverse=True)[1:6]

    # Fetch Book Index
    indx = np.where(xdf_pivot.index == search)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[indx])),
                           key=lambda x:x[1], reverse=True)[1:6]
    data = []
    for i in similar_books:
        item = []
        temp_df = dfbooks[dfbooks['Book-Title'] == xdf_pivot.index[i[0]] ]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))        
        data.append(item)
    
    return data


if __name__ == '__main__':
    dfbooks = pd.read_csv("Books.csv")
    dfratings = pd.read_csv("Ratings.csv")
    dfusers = pd.read_csv("Users.csv")

    # Verify the Dataset Number of Rows and Columns
    print("Books Shape: ", dfbooks.shape)
    print("Ratings Shape: ", dfratings.shape)
    print("Users Shape: ", dfusers.shape)
    print('='*20, ' COLUMNS ', '='*20)
    print('\n', '-'*20, '1. Books ', '-'*20)
    print(dfbooks.columns)
    print('\n', '-'*20, '2. Ratings ', '-'*20)
    print(dfratings.columns)
    print('\n', '-'*20, '3. Users ', '-'*20)
    print(dfusers.columns)
    print('\n\n')
    print('='*20, ' MISSING VALUES ', '='*20)
    print('\n', '-'*20, '1. Books ', '-'*20)
    print(dfbooks.isna().sum() )
    print('\n', '-'*20, '2. Ratings ', '-'*20)
    print(dfratings.isna().sum() )
    print('\n', '-'*20, '3. Users ', '-'*20)
    print(dfusers.isna().sum())

    dfbooks_rating = dfbooks.merge(dfratings, on = 'ISBN')
    print("\nShape: ", dfbooks_rating.shape )

    print("\n\n")
    print('\n', '-'*15, ' Dataset Info ', '-'*15, '\n')
    dfbooks_rating.info()

    print("\n\n")
    print('\n', '-'*15, ' Dataset ', '-'*15, '\n')
    dfbooks_rating.head()

    # Input the Name of Book While it returns the Similar Book Name
    # with its respective information like Author Name and Image URL
    cf_recommender("Harry Potter and the Sorcerer's Stone (Book 1)")