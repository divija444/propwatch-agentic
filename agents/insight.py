class InsightAgent:

    def generate_insights(self, hotspots):

        insights = []

        for _, row in hotspots.head(5).iterrows():

            region = row["RegionName"]
            state = row["StateName"]
            growth = round(row["rent_change_pct"] * 100, 2)

            #insight = f"{region}, {state} shows strong rent growth of {growth}%"
            insight = f"{region}, {state} shows strong rent growth of {growth}%"
            insights.append(insight)

        return insights