import cv2

def highlight_regions(image_path, ranked_items):

    image = cv2.imread(image_path)

    top_items = ranked_items[:5]

    for item in top_items:

        coords = item["coords"]

        x1 = int(coords[0][0])
        y1 = int(coords[0][1])

        x2 = int(coords[2][0])
        y2 = int(coords[2][1])

        attention = round(item["attention"], 2)

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            f"A:{attention}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    output_path = "outputs/cognitive_attention.png"

    cv2.imwrite(output_path, image)

    return output_path
