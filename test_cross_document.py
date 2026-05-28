from cross_document_engine import (
    analyze_cross_document_patterns
)

patterns = analyze_cross_document_patterns()

print("\nCROSS-DOCUMENT ANALYSIS:\n")

for item in patterns:

    print("=" * 60)

    print("CONCEPT:")

    print(item["concept"])

    print("\nAPPEARS IN:")

    print(item["source_count"])

    print("documents")

    print("\nSOURCES:")

    print(item["sources"])
    