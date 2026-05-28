from temporal_engine import (
    analyze_temporal_patterns
)

patterns = analyze_temporal_patterns()

print("\nTEMPORAL CONCEPT EVOLUTION:\n")

for concept, strength in patterns:

    print("=" * 60)

    print("CONCEPT:")

    print(concept)

    print("\nSTRENGTH:")

    print(round(strength, 2))
    