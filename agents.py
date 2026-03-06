from config import PLAYERS, TEAM

def player_analysis_agent(state):

    analysis = []

    for p in PLAYERS:
        analysis.append(f"{p} is performing well this season.")

    return {"player_analysis": analysis}


def team_analysis_agent(state):

    return {
        "team_analysis": f"{TEAM} has strong attacking players but needs defensive improvement."
    }


def strategy_agent(state):

    return {
        "strategy": "Use a 4-3-3 formation with aggressive pressing."
    }


def prediction_agent(state):

    return {
        "prediction": "Dream FC has a high chance of winning the next match."
    }


def commentary_agent(state):

    return {
        "commentary": "What an exciting match! The forwards are dominating the field."
    }