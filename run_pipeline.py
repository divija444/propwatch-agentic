from controller import PipelineController
from analytics.maps.rent_growth_map import generate_rent_growth_map
from analytics.models.rent_forecast import forecast_rent


def main():

    controller = PipelineController()

    result = controller.run()

    # Hotspots
    if "hotspots" in result:
        print("\nTop Hotspots:")
        print(result["hotspots"].head(10))

    # Spatial
    if "spatial_summary" in result:
        print("\nTop Growing States:")
        print(result["spatial_summary"].head(10))

    # Affordability
    if "expensive_regions" in result:
        print("\nMost Expensive Regions:")
        print(result["expensive_regions"].head(10))

    # Insights
    if "insights" in result:
        print("\nMarket Insights:")
        for insight in result["insights"]:
            print(insight)

    # GIS Map
    if "df_drift" in result:
        print("\nGenerating Rent Growth Map...")
        generate_rent_growth_map(result["df_drift"])

    # Forecast
    if "df_drift" in result:
        print("\nRent Forecast Example:")
        forecast_rent(result["df_drift"], "Los Angeles, CA")

    print("\nPipeline Complete")


if __name__ == "__main__":
    main()