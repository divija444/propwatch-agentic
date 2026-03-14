
class Constitution:

    def validate_dataframe(self, df):
        if df is None:
            raise ValueError("Dataframe cannot be None")

        if df.empty:
            raise ValueError("Dataframe is empty")

        return True

    def validate_columns(self, df, required_cols):

        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        return True