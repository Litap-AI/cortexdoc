from ocr_engine import extract_text
from structure_engine import group_text_blocks
from learning_engine import discover_topics

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

paragraphs = group_text_blocks(
    ocr_results
)

topics = discover_topics(
    paragraphs,
    n_clusters=3
)

for topic, texts in topics.items():

    print("\n" + "=" * 60)

    print(f"TOPIC {topic}")

    print("=" * 60)

    for text in texts[:3]:

        print("\n-", text[:300])
        