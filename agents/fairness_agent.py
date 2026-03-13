class FairnessAgent:

    def detect_unfair_growth(self, df, threshold=0.1):

        unfair = df[df["rent_change_pct"] > threshold]

        print("\nPotential Housing Risk Areas:")
        print(unfair[["RegionName","StateName","rent_change_pct"]].head(10))

        return unfair
