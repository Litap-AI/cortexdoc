from graph_analysis import (
    analyze_graph
)

results = analyze_graph()

print("\nKNOWLEDGE GRAPH ANALYSIS:\n")

for item in results[:10]:

    print("=" * 60)

    print("CONCEPT:")

    print(item["concept"])

    print("\nCONNECTIONS:")

    print(item["connections"])

    print("\nRELATED CONCEPTS:")

    print(item["related"])
    