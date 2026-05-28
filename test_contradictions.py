from contradiction_engine import (
    detect_contradictions
)

results = detect_contradictions()

print("\nCONTRADICTION ANALYSIS:\n")

for item in results:

    print("=" * 60)

    print("QUERY:")

    print(item["query"])

    print("\nSOURCE 1:")

    print(item["source_1"])

    print(item["answer_1"])

    print("\nSOURCE 2:")

    print(item["source_2"])

    print(item["answer_2"])
    