import folium

def generate_gis_map(df):

    m = folium.Map(location=[39.5, -98.35], zoom_start=4)

    for _, row in df.iterrows():

        if "lat" not in row or "lon" not in row:
            continue

        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=6,
            popup=f"{row['RegionName']} | Rent: ${row['Rent']}",
            color="red",
            fill=True
        ).add_to(m)

    m.save("data/outputs/housing_map.html")

    return m
