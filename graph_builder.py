from langgraph.graph import StateGraph, END
from agents import (
    player_analysis_agent,
    team_analysis_agent,
    strategy_agent,
    prediction_agent,
    commentary_agent
)

def build_graph():

    graph = StateGraph(dict)

    graph.add_node("player", player_analysis_agent)
    graph.add_node("team", team_analysis_agent)
    graph.add_node("strategy", strategy_agent)
    graph.add_node("prediction", prediction_agent)
    graph.add_node("commentary", commentary_agent)

    graph.set_entry_point("player")

    graph.add_edge("player", "team")
    graph.add_edge("team", "strategy")
    graph.add_edge("strategy", "prediction")
    graph.add_edge("prediction", "commentary")
    graph.add_edge("commentary", END)

    return graph.compile()
