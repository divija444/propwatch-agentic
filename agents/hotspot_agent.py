
import pandas as pd


class HotspotAgent:

    def rank_hotspots(self, df):

        # Remove rows where drift is NaN
        df = df.dropna(subset=["rent_change_pct"])

        # Calculate average growth per region
        growth = (
            df.groupby(["RegionName", "StateName"])["rent_change_pct"]
            .mean()
            .reset_index()
        )

        # Sort by highest growth
        growth = growth.sort_values(
            "rent_change_pct",
            ascending=False
        )

        # Return top 10 fastest growing regions
        return growth.head(10)