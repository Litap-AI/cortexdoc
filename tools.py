from memory_engine import query_memory

def search_memory(query):

    results = query_memory(query)

    return results["documents"][0]
