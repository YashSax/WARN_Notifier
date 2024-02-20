import read_database
import send_email
import pandas as pd
from fuzzywuzzy import fuzz

def get_state_df(state):
    return pd.read_csv(f"./formatted_warn/{state}.csv")

def notify_users():
    match_thresh = 60
    documents = read_database.get_documents_from_firebase()
    for d in documents:
        state = d._data["State"]
        company = d._data["Company"]
        df = get_state_df(state)
        df["match_score"] = [fuzz.ratio(i, company) for i in df["company_name"]]
        df = df.sort_values(by="match_score", ascending=False)
        df = df[df["match_score"] >= match_thresh]
        if len(df) > 0: 
            print(df.head())


if __name__ == "__main__":
    notify_users()