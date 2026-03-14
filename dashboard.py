import streamlit as st
import pandas as pd
import plotly.express as px
from controller import PipelineController
from langgraph.graph import StateGraph

st.set_page_config(page_title="Rental Market Analytics", layout="wide")

st.title("🏠 US Rental Market Analytics Dashboard")

st.write("Interactive analysis of US rental market trends using a multi-agent data pipeline.")

# Run pipeline
controller = PipelineController()
result = controller.run()

df_drift = result["df_drift"]
hotspots = result["hotspots"]
spatial = result["spatial_summary"]
expensive = result["expensive_regions"]

# -------------------------
# Top Hotspots
# -------------------------

st.header("🔥 Top Rent Growth Cities")

st.dataframe(hotspots.head(10))

fig_hotspots = px.bar(
    hotspots.head(10),
    x="RegionName",
    y="rent_change_pct",
    color="StateName",
    title="Top 10 Rental Growth Cities"
)

st.plotly_chart(fig_hotspots, use_container_width=True)

# -------------------------
# Growing States
# -------------------------

st.header("📈 Fastest Growing States")

st.dataframe(spatial.head(10))

fig_states = px.bar(
    spatial.head(10),
    x="StateName",
    y="rent_change_pct",
    title="Top Growing States"
)

st.plotly_chart(fig_states, use_container_width=True)

# -------------------------
# Most Expensive Regions
# -------------------------

st.header("💰 Most Expensive Rental Markets")

st.dataframe(expensive.head(10))

fig_expensive = px.bar(
    expensive.head(10),
    x="RegionName",
    y="Rent",
    color="StateName",
    title="Most Expensive Rental Markets"
)

st.plotly_chart(fig_expensive, use_container_width=True)

# -------------------------
# Rent Trend Visualization
# -------------------------

st.header("📊 Rent Trend Over Time")

cities = df_drift["RegionName"].unique()

selected_city = st.selectbox(
    "Select a City",
    cities
)

city_df = df_drift[df_drift["RegionName"] == selected_city]

fig_trend = px.line(
    city_df,
    x="Date",
    y="Rent",
    title=f"Rent Trend: {selected_city}"
)

st.plotly_chart(fig_trend, use_container_width=True)

st.success("Dashboard running successfully 🚀")