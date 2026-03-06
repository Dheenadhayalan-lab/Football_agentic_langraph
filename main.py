from graph_builder import build_graph

def main():

    graph = build_graph()

    result = graph.invoke({})

    print("\n⚽ Football Agentic AI Analyzer\n")

    print("Player Analysis:")
    for player in result["player_analysis"]:
        print("-", player)

    print("\nTeam Analysis:")
    print(result["team_analysis"])

    print("\nStrategy Suggestion:")
    print(result["strategy"])

    print("\nPrediction:")
    print(result["prediction"])

    print("\nAI Commentary:")
    print(result["commentary"])


if __name__ == "__main__":
    main()
