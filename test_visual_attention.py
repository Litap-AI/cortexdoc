from ocr_engine import extract_text
from semantic_engine import rank_relevance
from attention_engine import calculate_attention
from visualizer import highlight_regions

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

query = "important military strategy"

ranked = rank_relevance(
    query,
    ocr_results
)

for item in ranked:

    item["attention"] = calculate_attention(item)

final_ranked = sorted(
    ranked,
    key=lambda x: x["attention"],
    reverse=True
)

output = highlight_regions(
    "outputs/pages/page_1.png",
    final_ranked
)

print("Saved:", output)

print("\nTOP ATTENTION REGIONS:\n")

for item in final_ranked[:5]:

    print("=" * 50)

    print(item["text"])

    print("\nAttention:", round(item["attention"], 2))

    print("Relevance:", round(item["relevance"], 2))
    