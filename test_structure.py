from ocr_engine import extract_text
from structure_engine import group_text_blocks

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

paragraphs = group_text_blocks(
    ocr_results
)

for i, para in enumerate(paragraphs[:10]):

    print("=" * 60)

    print(f"PARAGRAPH {i+1}\n")

    print(para["text"])
    