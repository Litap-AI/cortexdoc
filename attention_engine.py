def calculate_attention(item):

    score = 0

    coords = item["coords"]

    x1 = coords[0][0]
    y1 = coords[0][1]

    x2 = coords[2][0]
    y2 = coords[2][1]

    width = x2 - x1
    height = y2 - y1

    area = width * height

    # Bigger text blocks attract attention
    score += area * 0.00005

    # OCR confidence matters
    score += item["confidence"] * 10

    # Top-of-page bias
    score += max(0, 1000 - y1) * 0.01

    # Semantic relevance matters most
    score += item["relevance"] * 50

    return score
