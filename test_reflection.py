from ocr_engine import extract_text
from semantic_engine import rank_relevance
from reflection_engine import detect_uncertainty

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

ranked = rank_relevance(
    "military strategy",
    ocr_results
)

for item in ranked[:20]:

    uncertainty = detect_uncertainty(item)

    print("=" * 50)

    print(item["text"])

    print("\nUncertainty:", uncertainty)

    if uncertainty >= 2:

        print("⚠️ Needs verification")
        