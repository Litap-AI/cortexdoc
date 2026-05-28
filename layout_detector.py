from ultralytics import YOLO
from huggingface_hub import hf_hub_download
import cv2

model_path = hf_hub_download(
    repo_id="juliozhao/DocLayout-YOLO-DocStructBench",
    filename="doclayout_yolo_docstructbench_imgsz1024.pt"
)

model = YOLO(model_path)

def detect_layout(image_path):

    image = cv2.imread(image_path)

    results = model(image_path)

    boxes = []

    for box in results[0].boxes:

        coords = box.xyxy.tolist()[0]

        confidence = float(box.conf.tolist()[0])

        cls = int(box.cls.tolist()[0])

        boxes.append({
            "coords": coords,
            "confidence": confidence,
            "class": cls
        })

    return image, boxes, results
