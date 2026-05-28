from knowledge_graph import (
    build_knowledge_graph
)

def analyze_graph():

    graph = build_knowledge_graph()

    ranked = []

    for concept, links in graph.items():

        ranked.append({

            "concept": concept,

            "connections": len(links),

            "related": list(links)
        })

    ranked = sorted(
        ranked,
        key=lambda x: x["connections"],
        reverse=True
    )

    return ranked
