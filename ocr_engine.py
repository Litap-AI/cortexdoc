from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def read_region(image_path):

    result = ocr.ocr(image_path)

    return result
