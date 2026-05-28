from ocr_engine import extract_text
from structure_engine import group_text_blocks
from memory_engine import (
    store_paragraphs,
    query_memory
)
from society_engine import (
    cognitive_society
)



ocr_results = extract_text(
    "outputs/pages/page_1.png"
)

paragraphs = group_text_blocks(
    ocr_results
)

store_paragraphs(paragraphs)

query = """
What military strategies
appear repeatedly?
"""

results = query_memory(query)

contexts = results["documents"][0]

society = cognitive_society(
    query,
    contexts
)

print("\nFINAL ANSWER:\n")

print(society["answer"])

print("\nSKEPTIC ANALYSIS:\n")

print(society["critique"])

print("\nRESEARCH PLAN:\n")

print(society["plan"])

print("\nEVIDENCE:\n")

print(society["evidence"])

print("\nDEBATE:\n")

for msg in society["debate"]:

    print(msg.display())

print("\nFINAL EVALUATION:\n")

print(society["evaluation"])

print("\nCONSENSUS ANSWER:\n")

print(society["consensus"])

