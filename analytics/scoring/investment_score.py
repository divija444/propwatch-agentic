def compute_investment_score(df):

    df["growth_score"] = df["rent_change_pct"]

    df["affordability_score"] = 1 / df["Rent"]

    df["investment_score"] = (
        0.4 * df["growth_score"] +
        0.3 * df["affordability_score"]
    )

    return df.sort_values("investment_score", ascending=False)
