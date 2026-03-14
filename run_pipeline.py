from controller import PipelineController
from analytics.maps.gis_map import generate_gis_map
from analytics.scoring.investment_score import compute_investment_score

print("Starting Pipeline...")

controller = PipelineController()

result = controller.run()

df = result["df_drift"]

print("Generating GIS Map...")

generate_gis_map(df)

print("Computing Investment Score...")

df = compute_investment_score(df)

print("Top Investment Markets:")

print(df[["RegionName","investment_score"]].head(10))

print("Pipeline Finished")
