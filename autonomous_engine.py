from curiosity_engine import (
    generate_curiosity
)

from memory_engine import (
    query_memory
)

from reasoning_engine import (
    reason_over_context
)

def autonomous_research_cycle():

    curiosity_items = generate_curiosity()

    reports = []

    for curiosity in curiosity_items:

        results = query_memory(
            curiosity
        )

        contexts = results["documents"][0]

        reasoning = reason_over_context(
            curiosity,
            contexts
        )

        reports.append({

            "curiosity": curiosity,

            "reasoning": reasoning
        })

    return reports
