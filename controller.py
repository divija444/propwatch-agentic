from agents.graph import graph


class PipelineController:

    def run(self):

        print("Starting Pipeline...\n")

        # Run the LangGraph pipeline
        result = graph.invoke({})

        print("\nPipeline Finished")

        return result