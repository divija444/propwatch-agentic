from agents.ingestion_agent import IngestionAgent
from agents.drift_agent import DriftAgent
from agents.hotspot_agent import HotspotAgent

DATA_PATH = "data/zori_us.csv"


def main():

    ingestion = IngestionAgent(DATA_PATH)
    drift = DriftAgent()
    hotspot_agent = HotspotAgent()

    
    df = ingestion.load_data()

    df_long = ingestion.wide_to_long(df)

    df_drift = drift.calculate_drift(df_long)

    hotspots = drift.detect_high_growth(df_drift)

    print("Drift Calculated")
    print(df_drift.head())

    print("\nHigh Growth Areas:")
    print(hotspots[["RegionName","StateName","Date","Rent","rent_change_pct"]].head(10))
    
    top_hotspots = hotspot_agent.rank_hotspots(df_drift)

    print("\nTop Hotspots:")
    print(top_hotspots)

if __name__ == "__main__":
    main()