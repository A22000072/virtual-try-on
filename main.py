import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Load virtual assets (e.g., hat, glasses)
hat = cv2.imread('./assets/hat.png', cv2.IMREAD_UNCHANGED)
glasses = cv2.imread('./assets/glasses.png', cv2.IMREAD_UNCHANGED)

# Validasi apakah gambar berhasil dimuat
if hat is None:
    print("Error: Hat image not found!")
    exit()

if glasses is None:
    print("Error: Glasses image not found!")
    exit()

def overlay_image(background, overlay, x, y, scale=1):
    """
    Overlay an image (with alpha) onto a background.
    """
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape

    # Validasi posisi overlay agar tidak keluar dari frame
    if x < 0 or y < 0 or x + w > background.shape[1] or y + h > background.shape[0]:
        print(f"Invalid position for overlay: x={x}, y={y}, w={w}, h={h}")
        return background

    alpha_overlay = overlay[:, :, 3] / 255.0  # Alpha channel
    alpha_background = 1.0 - alpha_overlay

    for c in range(0, 3):  # RGB Channels
        background[y:y+h, x:x+w, c] = (
            alpha_overlay * overlay[:, :, c] +
            alpha_background * background[y:y+h, x:x+w, c]
        )
    return background

# Start Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access camera.")
    exit()

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Flip frame horizontally for natural mirroring
        frame = cv2.flip(frame, 1)

        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        if results.detections:
            for detection in results.detections:
                # Get bounding box
                bboxC = detection.location_data.relative_bounding_box
                h, w, c = frame.shape
                bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                       int(bboxC.width * w), int(bboxC.height * h)

                x, y, w_box, h_box = bbox

                # Debug posisi bounding box
                print(f"Bounding Box: x={x}, y={y}, width={w_box}, height={h_box}")

                # Calculate coordinates for virtual assets
                hat_width = int(1.5 * w_box)  # Adjust hat width
                hat_x = max(0, x - (hat_width - w_box) // 2)
                hat_y = max(0, y - int(0.6 * h_box))

                glasses_width = int(w_box)
                glasses_x = max(0, x)
                glasses_y = max(0, y + int(0.3 * h_box))

                # Overlay virtual assets
                frame = overlay_image(frame, hat, hat_x, hat_y, scale=hat_width / hat.shape[1])
                frame = overlay_image(frame, glasses, glasses_x, glasses_y, scale=glasses_width / glasses.shape[1])

        # Show the frame
        cv2.imshow("Virtual Try-On", frame)

        # Press 'ESC' to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
