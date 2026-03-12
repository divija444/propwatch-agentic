import pandas as pd


class DriftAgent:

    def calculate_drift(self, df):

        # Remove rows where Rent is missing
        df = df.dropna(subset=["Rent"])

        # Convert Date column safely
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        # Remove rows where Date conversion failed
        df = df.dropna(subset=["Date"])

        # Sort values
        df = df.sort_values(["RegionName", "Date"])

        # Calculate percentage change
        df["rent_change_pct"] = df.groupby("RegionName")["Rent"].pct_change()

        return df


    def detect_high_growth(self, df, threshold=0.05):
        """
        Detect regions where rent increased more than threshold (5%)
        """

        hotspots = df[df["rent_change_pct"] > threshold]

        return hotspots
