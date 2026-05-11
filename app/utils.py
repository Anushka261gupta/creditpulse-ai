import pandas as pd

def load_invoices(file):

    df = pd.read_csv(file)

    return df