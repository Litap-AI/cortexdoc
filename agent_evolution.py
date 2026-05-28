from agent_memory import (
    load_agent_memory
)

def evolve_agents():

    memory = load_agent_memory()

    evolution = {}

    for agent, stats in memory.items():

        success = stats["success"]

        failure = stats["failure"]

        total = success + failure

        if total == 0:

            confidence = 0

        else:

            confidence = success / total

        evolution[agent] = {

            "confidence": round(
                confidence,
                2
            ),

            "strictness": round(
                1 - confidence,
                2
            )
        }

    return evolution
