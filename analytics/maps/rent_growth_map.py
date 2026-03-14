import pandas as pd
import folium
from geopy.geocoders import Nominatim
import time


def generate_rent_growth_map(df):

    geolocator = Nominatim(user_agent="rent_map")

    latest = (
        df.sort_values("Date")
        .groupby(["RegionName", "StateName"])
        .tail(1)
    )

    # Create US map
    m = folium.Map(location=[39.5, -98.35], zoom_start=4)

    # Only map top 20 hotspots to avoid slow geocoding
    latest = latest.sort_values("rent_change_pct", ascending=False).head(20)

    for _, row in latest.iterrows():

        city = f"{row['RegionName']}, {row['StateName']}"

        try:
            location = geolocator.geocode(city)

            if location:

                popup = f"{city}<br>Growth: {row['rent_change_pct']:.2%}"

                folium.CircleMarker(
                    location=[location.latitude, location.longitude],
                    radius=6,
                    popup=popup,
                    color="red",
                    fill=True
                ).add_to(m)

            time.sleep(1)  # prevent API blocking

        except:
            continue

    m.save("data/outputs/rent_growth_map.html")

    print("Map saved to data/outputs/rent_growth_map.html")