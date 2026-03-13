from langgraph.graph import StateGraph
from agents.ingestion_agent import IngestionAgent
from agents.drift_agent import DriftAgent
from agents.hotspot_agent import HotspotAgent
from agents.spatial_agent import SpatialAgent
from agents.affordability_agent import AffordabilityAgent

ingestion = IngestionAgent("data/zori_us.csv")
drift = DriftAgent()
hotspot = HotspotAgent()
spatial = SpatialAgent()
affordability = AffordabilityAgent()


def ingestion_node(state):

    df = ingestion.load_data()
    df_long = ingestion.wide_to_long(df)

    return {**state, "df_long": df_long}


def drift_node(state):

    df_drift = drift.calculate_drift(state["df_long"])

    return {**state, "df_drift": df_drift}


def hotspot_node(state):

    hotspots = hotspot.rank_hotspots(state["df_drift"])

    return {**state, "hotspots": hotspots}


def spatial_node(state):

    spatial_summary = spatial.analyze_spatial_patterns(state["df_drift"])

    return {**state, "spatial_summary": spatial_summary}

def affordability_node(state):

    expensive_regions = affordability.detect_expensive_regions(state["df_drift"])

    return {**state, "expensive_regions": expensive_regions}


builder = StateGraph(dict)

builder.add_node("ingestion", ingestion_node)
builder.add_node("drift", drift_node)
builder.add_node("hotspot", hotspot_node)
builder.add_node("spatial", spatial_node)
builder.add_node("affordability", affordability_node)

builder.set_entry_point("ingestion")

builder.add_edge("ingestion", "drift")
builder.add_edge("drift", "hotspot")
builder.add_edge("hotspot", "spatial")
builder.add_edge("spatial", "affordability")

graph = builder.compile()