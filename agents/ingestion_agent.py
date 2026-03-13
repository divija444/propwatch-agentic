import pandas as pd


class IngestionAgent:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        df = pd.read_csv(self.path)
        return df

    def wide_to_long(self, df):

        metadata_cols = [
            "RegionID",
            "SizeRank",
            "RegionName",
            "RegionType",
            "StateName"
        ]

        df_long = df.melt(
            id_vars=metadata_cols,
            var_name="Date",
            value_name="Rent"
        )

        # Convert Date column
        df_long["Date"] = pd.to_datetime(df_long["Date"])

        return df_long