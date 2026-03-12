from agents.ingestion_agent import IngestionAgent

DATA_PATH = "data/zori_us.csv"

def main():

    ingestion = IngestionAgent(DATA_PATH)

    df = ingestion.load_data()

    df_long = ingestion.wide_to_long(df)

    print("Dataset Loaded")
    print(df_long.head())


if __name__ == "__main__":
    main()