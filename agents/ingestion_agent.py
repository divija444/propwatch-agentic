import pandas as pd

class IngestionAgent:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        df = pd.read_csv(self.path)
        return df

    def wide_to_long(self, df):
        df_long = df.melt(
            id_vars=["RegionName"],
            var_name="Date",
            value_name="Rent"
        )
        return df_long