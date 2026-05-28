from agent_memory import (
    update_agent_score
)

from agent_evolution import (
    evolve_agents
)

update_agent_score(
    "Reasoner",
    success=True
)

update_agent_score(
    "Skeptic",
    success=False
)

update_agent_score(
    "Moderator",
    success=True
)

results = evolve_agents()

print("\nAGENT EVOLUTION:\n")

for agent, stats in results.items():

    print("=" * 60)

    print(agent)

    print("\nConfidence:")

    print(stats["confidence"])

    print("\nStrictness:")

    print(stats["strictness"])
    