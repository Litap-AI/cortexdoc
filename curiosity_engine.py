from persistent_memory import (
    load_memory
)

def generate_curiosity():

    memory = load_memory()

    curiosity = []

    for item in memory:

        weight = item["weight"]

        query = item["query"]

        evaluation = item["evaluation"]

        score = evaluation["score"]

        # Weak confidence
        if score <= 1:

            curiosity.append(
                f"Investigate weak evidence for: {query}"
            )

        # Strong recurring concepts
        elif weight >= 2:

            curiosity.append(
                f"Explore deeper implications of: {query}"
            )

    return curiosity
