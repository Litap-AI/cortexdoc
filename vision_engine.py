from transformers import pipeline

image_captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

def analyze_image(image_path):

    result = image_captioner(image_path)

    return result[0]["generated_text"]
