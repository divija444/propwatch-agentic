class AffordabilityAgent:

    def detect_expensive_regions(self, df):

        latest = (
            df.sort_values("Date")
            .groupby(["RegionName", "StateName"])
            .tail(1)
        )

        expensive = latest.sort_values("Rent", ascending=False)

        return expensive