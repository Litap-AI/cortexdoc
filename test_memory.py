from ocr_engine import extract_text
from structure_engine import group_text_blocks
from memory_engine import (
    store_paragraphs,
    query_memory
)

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

paragraphs = group_text_blocks(
    ocr_results
)

store_paragraphs(paragraphs)

results = query_memory(
    "important military strategy"
)

print(results)
