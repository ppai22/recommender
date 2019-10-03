import pandas as pd


def read_data():

    """
    Obj: Method that returns the relevant dataset from the MovieLens data files
    Parameters: -
    Returns: Dataframe in required format
    """

    # Path to dataset
    file_path = r"D:\\Python\\Datasets\\MovieLens100k\\movielens-100k-dataset\\ml-100k\\u.data"
    col_names = ["user-id", "item-id", "rating", "timestamp"]

    # Path to item-id -> title mapping dataset
    movie_names_path = r"D:\\Python\\Datasets\\MovieLens100k\\movielens-100k-dataset\\ml-100k\\u.item"
    m_col_names = ["item-id", "title", "release_date", "video_release_date", "imdb_url"]

    # Reading the MovieLens dataset
    dataset = pd.read_csv(file_path, header=None, sep="\t", names=col_names)
    # Reading the title -> item-id mapping data
    movies = pd.read_csv(movie_names_path, sep="|", names=m_col_names, usecols=range(5), encoding="latin-1")

    # Merging both the data
    data = pd.merge(dataset, movies)

    # Filtering out only the required data
    reqd_data = data.drop(["item-id", "timestamp", "release_date", "video_release_date", "imdb_url"], axis=1)


    # Generating the matrix with user-ids as rows and movies as the columns with rating for each movie by the user
    matrix = reqd_data.pivot_table(index=["user-id"], columns=["title"], values="rating")

    return matrix
