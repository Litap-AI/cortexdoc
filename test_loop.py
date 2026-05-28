from ocr_engine import extract_text
from structure_engine import group_text_blocks
from memory_engine import (
    store_paragraphs
)
from loop_engine import cognitive_loop

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

paragraphs = group_text_blocks(
    ocr_results
)

store_paragraphs(paragraphs)

query = """
What military strategies
appear repeatedly in this document?
"""

final_answer = cognitive_loop(
    query,
    iterations=3
)

print("\nFINAL ANSWER:\n")

print(final_answer)
