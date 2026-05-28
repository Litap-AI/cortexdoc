def detect_uncertainty(item):

    score = 0

    # Low OCR confidence
    if item["confidence"] < 0.85:
        score += 1

    # Weak semantic relevance
    if item["relevance"] < 0.30:
        score += 1

    # Very short text fragments
    if len(item["text"].split()) < 4:
        score += 1

    return score
