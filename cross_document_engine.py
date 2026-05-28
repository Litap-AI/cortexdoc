from persistent_memory import (
    load_memory
)

def analyze_cross_document_patterns():

    memory = load_memory()

    patterns = {}

    for item in memory:

        source = item["source"]

        query = item["query"]

        if query not in patterns:

            patterns[query] = []

        patterns[query].append(source)

    analysis = []

    for query, sources in patterns.items():

        unique_sources = list(set(sources))

        analysis.append({

            "concept": query,

            "source_count": len(unique_sources),

            "sources": unique_sources
        })

    return analysis
