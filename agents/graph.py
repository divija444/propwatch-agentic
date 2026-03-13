from langgraph.graph import StateGraph
from agents.ingestion_agent import IngestionAgent
from agents.drift_agent import DriftAgent
from agents.hotspot_agent import HotspotAgent

# Initialize agents
ingestion = IngestionAgent("data/zori_us.csv")
drift = DriftAgent()
hotspot = HotspotAgent()


# -----------------------
# Nodes
# -----------------------

def ingestion_node(state):

    df = ingestion.load_data()
    df_long = ingestion.wide_to_long(df)

    return {"df_long": df_long}


def drift_node(state):

    df_drift = drift.calculate_drift(state["df_long"])

    return {"df_drift": df_drift}


def hotspot_node(state):

    hotspots = hotspot.rank_hotspots(state["df_drift"])

    return {"hotspots": hotspots}


# -----------------------
# Graph Definition
# -----------------------

builder = StateGraph(dict)

builder.add_node("ingestion", ingestion_node)
builder.add_node("drift", drift_node)
builder.add_node("hotspot", hotspot_node)

builder.set_entry_point("ingestion")

builder.add_edge("ingestion", "drift")
builder.add_edge("drift", "hotspot")

graph = builder.compile()