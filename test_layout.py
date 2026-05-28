from layout_detector import detect_layout
import cv2

image, results = detect_layout(
    "outputs/pages/page_1.png"
)

annotated = results[0].plot()

cv2.imwrite(
    "outputs/layout_detected.png",
    annotated
)

print("Layout detection completed!")
