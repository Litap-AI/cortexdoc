from ocr_engine import extract_text

results = extract_text(
    "outputs/pages/page_1.png"
)

for item in results[:20]:

    print("=" * 50)

    print("TEXT:")
    print(item["text"])

    print("\nCONFIDENCE:")
    print(item["confidence"])

    print("\nCOORDS:")
    print(item["coords"])
    