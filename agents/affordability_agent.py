class AffordabilityAgent:

    def detect_expensive_regions(self, df):

        # Get latest rent for each city
        latest = (
            df.sort_values("Date")
            .groupby(["RegionName", "StateName"])
            .tail(1)
        )

        # Sort by rent
        expensive = latest.sort_values("Rent", ascending=False)

        print("\nMost Expensive Regions:")
        print(expensive[["RegionName","StateName","Rent"]].head(10))

        return expensive