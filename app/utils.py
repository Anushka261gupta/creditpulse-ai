import pandas as pd

def load_invoices(csv_path):

    df = pd.read_csv(csv_path)

    return df