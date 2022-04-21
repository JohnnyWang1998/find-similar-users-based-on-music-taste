
import pandas as pd


def to_numeric(_df: pd.DataFrame):
    """
    Convert object column to int collumn to reduce memory usage
    @param _df: dataframe
    return: numeric dataframe
    """
    df = _df[['userid', 'artist_track']].copy()

    unique_user = df.userid.unique()
    unique_track = df.artist_track.unique()
    user_dict = {}
    track_dict = {}
    for (i, j) in enumerate(unique_user):
        user_dict[j] = i
    for (i, j) in enumerate(unique_track):
        track_dict[j] = i

    df.userid.replace(user_dict, inplace=True)
    df.artist_track.replace(track_dict, inplace=True)
    return df
