from ocr_engine import extract_text
from semantic_engine import rank_relevance

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

query = "important military strategy"

ranked = rank_relevance(
    query,
    ocr_results
)

for item in ranked[:10]:

    print("=" * 50)

    print("TEXT:")
    print(item["text"])

    print("\nRELEVANCE:")
    print(item["relevance"])
    