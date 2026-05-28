import time

from PIL import Image

from paddleocr import PaddleOCR

ocr = PaddleOCR(

    use_angle_cls=True,
    
    lang='en',
    
    ocr_version='PP-OCRv4'


)
def optimize_image(image_path):

    image = Image.open(image_path)

    max_width = 500

    if image.width > max_width:

        ratio = max_width / image.width

        new_height = int(
            image.height * ratio
        )

        image = image.resize(
            (max_width, new_height)
        )

    optimized_path = "outputs/optimized_page.png"

    image.save(optimized_path)

    return optimized_path



def extract_text(image_path):

    start = time.time()
    print("\nLOADING OCR ENGINE...\n")

    optimized = optimize_image(
    image_path
)

    print("\nIMAGE OPTIMIZED\n")

    result = ocr.predict(
    optimized
)
    result = result[:20]


    print("\nOCR RAW RESULT RECEIVED\n")

    extracted = []
    

    for item in result:

     texts = item.get(
        "rec_texts",
        []
    )

    scores = item.get(
        "rec_scores",
        []
    )

    for text, confidence in zip(
        texts,
        scores
    ):

        extracted.append({

            "text": text,

            "confidence": confidence,
            "coords": [
                [0, 0],
                [0, 0]
            ]
        })

    print("\nTEXT EXTRACTION FINISHED\n")
    end = time.time()

    print(f"\nOCR TIME: {end - start:.2f} seconds\n")

    return extracted

