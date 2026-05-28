from persistent_memory import (
    load_memory
)

def analyze_temporal_patterns():

    memory = load_memory()

    concept_strength = {}

    for item in memory:

        query = item["query"]

        weight = item["weight"]

        if query not in concept_strength:

            concept_strength[query] = 0

        concept_strength[query] += weight

    ranked = sorted(
        concept_strength.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked
