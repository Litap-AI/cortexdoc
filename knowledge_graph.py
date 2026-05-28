from persistent_memory import (
    load_memory
)

def build_knowledge_graph():

    memory = load_memory()

    graph = {}

    for item in memory:

        query = item["query"]

        words = query.lower().split()

        for word in words:

            if word not in graph:

                graph[word] = set()

            for related in words:

                if related != word:

                    graph[word].add(related)

    return graph
