import pandas as pd

class SpatialAgent:

    def analyze_spatial_patterns(self, df):

        spatial_summary = (
            df.groupby(["StateName"])["rent_change_pct"]
            .mean()
            .reset_index()
        )

        spatial_summary = spatial_summary.sort_values(
            "rent_change_pct",
            ascending=False
        )

        return spatial_summary