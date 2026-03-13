from agents.graph import graph
from agents.insight import InsightAgent


def main():

    # Run the LangGraph pipeline
    result = graph.invoke({})

    print("\nPipeline Finished")

    # -------------------------
    # Top Hotspots
    # -------------------------
    if "hotspots" in result:

        hotspots = result["hotspots"]

        print("\nTop Hotspots:")
        print(hotspots.head(10))

        # -------------------------
        # Market Insights
        # -------------------------
        insight_agent = InsightAgent()
        insights = insight_agent.generate_insights(hotspots)

        print("\nMarket Insights:")
        for insight in insights:
            print(insight)

    # -------------------------
    # Top Growing States
    # -------------------------
    if "spatial_summary" in result:

        spatial_summary = result["spatial_summary"]

        print("\nTop Growing States:")
        print(spatial_summary.head(10))
    
# -------------------------
# Most Expensive Regions
# -------------------------
    if "expensive_regions" in result:

        print("\nMost Expensive Regions:")
        print(result["expensive_regions"].head(10))


if __name__ == "__main__":
    main()