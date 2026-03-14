import streamlit as st
import pandas as pd
import plotly.express as px
import us

from controller import PipelineController
from analytics.scoring.investment_score import compute_investment_score
from ai.insight_generator import generate_market_insights
from ai.housing_llm_assistant import ask_housing_llm


# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------

st.set_page_config(
    page_title="PropWatch AI Housing Intelligence",
    layout="wide"
)

st.title("🏠 PropWatch AI Housing Intelligence Platform")

st.markdown(
"""
Analyze **U.S. rental housing markets** using AI.

This platform helps identify:

• 📈 Fast growing rental markets  
• 💰 Expensive cities  
• 🏆 Best places for property investment  
• 🤖 AI-generated market insights
"""
)

# ---------------------------------------------------
# RUN DATA PIPELINE
# ---------------------------------------------------

controller = PipelineController()
result = controller.run()

df = result["df_drift"].copy()

# ---------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------

df = df.dropna(subset=["Rent"])

df["rent_change_pct"] = df["rent_change_pct"].fillna(0)

df["RentGrowthPercent"] = df["rent_change_pct"] * 100


# ---------------------------------------------------
# STATE NAME CONVERSION
# ---------------------------------------------------

def full_state_name(abbr):

    try:
        if pd.isna(abbr):
            return "Unknown"

        state = us.states.lookup(str(abbr))

        return state.name if state else abbr

    except:
        return abbr


df["StateFull"] = df["StateName"].apply(full_state_name)

# ---------------------------------------------------
# INVESTMENT SCORE
# ---------------------------------------------------

df = compute_investment_score(df)

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("📍 Filters")

states = sorted(df["StateFull"].dropna().unique())

selected_states = st.sidebar.multiselect(
    "Select States",
    states,
    default=states[:5]
)

filtered_df = df[df["StateFull"].isin(selected_states)]

# ---------------------------------------------------
# MARKET OVERVIEW
# ---------------------------------------------------

st.subheader("📊 Market Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Cities Analyzed",
    len(filtered_df)
)

col2.metric(
    "Average Rent",
    f"${round(filtered_df['Rent'].mean(),2)}"
)

col3.metric(
    "Average Rent Growth",
    f"{round(filtered_df['RentGrowthPercent'].mean(),2)}%"
)

col4.metric(
    "Highest Rent",
    f"${round(filtered_df['Rent'].max(),2)}"
)

st.divider()

# ---------------------------------------------------
# FASTEST GROWING CITIES
# ---------------------------------------------------

st.subheader("📈 Fastest Growing Rental Markets")

top_growth = (
    filtered_df
    .sort_values("RentGrowthPercent", ascending=False)
    .head(20)
)

fig_growth = px.bar(
    top_growth,
    x="RentGrowthPercent",
    y="RegionName",
    orientation="h",
    color="RentGrowthPercent",
    labels={
        "RegionName": "City",
        "RentGrowthPercent": "Rent Growth (%)"
    }
)

st.plotly_chart(fig_growth, use_container_width=True)

# ---------------------------------------------------
# INVESTMENT OPPORTUNITIES
# ---------------------------------------------------

st.subheader("🏆 Best Cities for Property Investment")

top_invest = (
    filtered_df
    .sort_values("investment_score", ascending=False)
    .head(15)
)

st.dataframe(
    top_invest[[
        "RegionName",
        "StateFull",
        "Rent",
        "RentGrowthPercent",
        "investment_score"
    ]].rename(columns={
        "RegionName": "City",
        "StateFull": "State",
        "Rent": "Average Rent ($)",
        "RentGrowthPercent": "Rent Growth (%)",
        "investment_score": "Investment Score"
    }),
    use_container_width=True
)

# ---------------------------------------------------
# RENT TREND EXPLORER
# ---------------------------------------------------

st.subheader("📊 Rent Explorer")

city = st.selectbox(
    "Select City",
    filtered_df["RegionName"].unique()
)

city_df = df[df["RegionName"] == city]

if "Date" in city_df.columns:

    fig_trend = px.line(
        city_df,
        x="Date",
        y="Rent",
        title=f"Rent Trend in {city}"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

# ---------------------------------------------------
# AI MARKET INSIGHTS
# ---------------------------------------------------

st.subheader("🤖 AI Market Insights")

if st.button("Generate AI Market Report"):

    insights = generate_market_insights(filtered_df)

    st.write(insights)

# ---------------------------------------------------
# DATA EXPLORER
# ---------------------------------------------------

st.subheader("📁 Explore Data")

st.dataframe(filtered_df)

# ---------------------------------------------------
# AI HOUSING ASSISTANT
# ---------------------------------------------------

st.sidebar.divider()

st.sidebar.header("🤖 Ask the Housing AI")

question = st.sidebar.text_input(
    "Ask a question about housing markets"
)

if question:

    answer = ask_housing_llm(question, filtered_df)

    st.sidebar.write(answer)

st.sidebar.markdown(
"""
Example questions:

• Which cities have fastest rent growth?  
• What are the best investment markets?  
• Which states have rising housing demand?
"""
)

st.success("Dashboard loaded successfully 🚀")
