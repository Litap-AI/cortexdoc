from ocr_engine import extract_text
from semantic_engine import rank_relevance
from attention_engine import calculate_attention

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

query = "important military strategy"

ranked = rank_relevance(
    query,
    ocr_results
)

for item in ranked:

    attention = calculate_attention(item)

    item["attention"] = attention

final_ranked = sorted(
    ranked,
    key=lambda x: x["attention"],
    reverse=True
)

for item in final_ranked[:10]:

    print("=" * 60)

    print("TEXT:")
    print(item["text"])

    print("\nRELEVANCE:")
    print(round(item["relevance"], 3))

    print("\nATTENTION:")
    print(round(item["attention"], 3))
    