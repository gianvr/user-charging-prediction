import pandas as pd


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.drop(columns=['Charging Start Time', 'Charging End Time', 'User ID', 'Charging Station ID'])
    data = data[data["User Type"] != "Commuter"]
    return data
