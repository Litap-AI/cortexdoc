def group_text_blocks(blocks, y_threshold=25):

    blocks = sorted(
        blocks,
        key=lambda x: (
            x["coords"][0][1],
            x["coords"][0][0]
        )
    )

    grouped = []

    current_group = []

    last_y = None

    for block in blocks:

        y = block["coords"][0][1]

        if last_y is None:

            current_group.append(block)

        elif abs(y - last_y) < y_threshold:

            current_group.append(block)

        else:

            grouped.append(current_group)

            current_group = [block]

        last_y = y

    if current_group:

        grouped.append(current_group)

    paragraphs = []

    for group in grouped:

        text = " ".join([
            item["text"]
            for item in group
        ])

        paragraphs.append({
            "text": text,
            "blocks": group
        })

    return paragraphs
