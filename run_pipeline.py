from agents.ingestion_agent import IngestionAgent
from agents.drift_agent import DriftAgent

DATA_PATH = "data/zori_us.csv"


def main():

    ingestion = IngestionAgent(DATA_PATH)
    drift = DriftAgent()

    df = ingestion.load_data()

    df_long = ingestion.wide_to_long(df)

    df_drift = drift.calculate_drift(df_long)

    hotspots = drift.detect_high_growth(df_drift)

    print("Drift Calculated")
    print(df_drift.head())

    print("\nHigh Growth Areas:")
    print(hotspots[["RegionName","StateName","Date","Rent","rent_change_pct"]].head(10))


if __name__ == "__main__":
    main()