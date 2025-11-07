# main.py
from models.face_recognizer import FaceRecognizer
from config.settings import Settings

def main():
    app = FaceRecognizer(Settings)
    app.run_camera_verification()

if __name__ == "__main__":
    main()
# config/settings.py
import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Paths
    REFERENCE_DIR = os.path.join(BASE_DIR, "data", "reference")
    REFERENCE_PATHS = [os.path.join(REFERENCE_DIR, "reference.jpg")]
    LOG_DIR = os.path.join(BASE_DIR, "data", "logs")

    # DeepFace configuration
    MODEL_NAME = "ArcFace"
    DETECTOR_BACKENDS = ["retinaface", "mtcnn", "opencv"]
    COSINE_THRESHOLD = 0.35

    # Camera configuration
    FRAME_SKIP = 30
    CAM_INDEX = 0

