def score_block(block):

    score = 0

    if block.type == "Title":
        score += 10

    if block.type == "Table":
        score += 7

    if block.coordinates[1] < 300:
        score += 3

    return score
