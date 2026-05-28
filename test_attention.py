from layout_detector import detect_layout
from attention_engine import calculate_attention

image, boxes, results = detect_layout(
    "outputs/pages/page_1.png"
)

for i, box in enumerate(boxes):

    score = calculate_attention(box)

    print(f"Region {i+1}")
    print(f"Coords: {box['coords']}")
    print(f"Confidence: {box['confidence']:.2f}")
    print(f"Attention Score: {score:.2f}")
    print("-" * 40)
    