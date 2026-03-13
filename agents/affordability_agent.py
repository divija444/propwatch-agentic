class AffordabilityAgent:

    def detect_expensive_regions(self, df):

        expensive = df.sort_values("Rent", ascending=False)

        print("\nMost Expensive Regions:")
        print(expensive[["RegionName","StateName","Rent"]].head(10))

        return expensive
