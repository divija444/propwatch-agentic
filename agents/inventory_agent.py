class InventoryAgent:

    def analyze_inventory(self, df):

        inventory = df.groupby("RegionName").size().reset_index(name="observations")

        inventory = inventory.sort_values("observations", ascending=False)

        print("\nRegions with Most Data Points:")
        print(inventory.head(10))

        return inventory
