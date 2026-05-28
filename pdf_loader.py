import fitz
import os

def pdf_to_images(pdf_path, output_folder="outputs/pages"):

    doc = fitz.open(pdf_path)

    os.makedirs(output_folder, exist_ok=True)

    image_paths = []

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)

        pix = page.get_pixmap(dpi=150)

        img_path = f"{output_folder}/page_{page_num + 1}.png"

        pix.save(img_path)

        image_paths.append(img_path)

    return image_paths

