import gradio as gr

import time

from ocr_engine import extract_text

from structure_engine import (
    group_text_blocks
)

from memory_engine import (
    store_paragraphs,
    query_memory
)

from reasoning_engine import (
    reason_over_context
)

def analyze_pdf(query):

    print("\n========== START ==========\n")

    print("QUERY:")
    print(query)

    ocr_start = time.time()

    ocr_results = extract_text(
        "outputs/pages/page_1.png"
    )
    ocr_end = time.time()
    
    print(
    f"\nOCR STAGE: {ocr_end - ocr_start:.2f}s\n"
)

    print("\nOCR RESULTS:")
    print(ocr_results[:5])

    paragraphs = group_text_blocks(
        ocr_results
    )

    print("\nPARAGRAPHS:")
    print(paragraphs[:3])

    store_paragraphs(paragraphs)

    results = query_memory(query)

    print("\nMEMORY RESULTS:")
    print(results)

    contexts = results["documents"][0]

    print("\nCONTEXTS:")
    print(contexts)

    answer = reason_over_context(
        query,
        contexts
    )

    print("\nFINAL ANSWER:")
    print(answer)

    print("\n========== END ==========\n")

    return answer



interface = gr.Interface(

    fn=analyze_pdf,

    inputs="text",

    outputs="text",

    title="CortexDoc",

    description="""
Cognitive Document Intelligence System
"""
)

interface.launch()
