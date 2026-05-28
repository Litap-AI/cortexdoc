from ocr_engine import extract_text
from structure_engine import group_text_blocks
from memory_engine import (
    store_paragraphs,
    query_memory
)
from reasoning_engine import (
    reason_over_context
)

ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

paragraphs = group_text_blocks(
    ocr_results
)

store_paragraphs(paragraphs)

query = "What important military strategies are discussed?"

results = query_memory(query)

contexts = results["documents"][0]

answer = reason_over_context(
    query,
    contexts
)

print("\nANSWER:\n")

print(answer)
