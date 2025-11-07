# models/face_recognizer.py
import cv2
import numpy as np
import os
from deepface import DeepFace
from utils.helpers import cosine_distance

class FaceRecognizer:
    def __init__(self, config):
        self.config = config
        self.reference_embeddings = []
        self.detector_backend_used = config.DETECTOR_BACKENDS[0]
        self._prepare_reference_embeddings()

    def _prepare_reference_embeddings(self):
        print("Preparing reference embeddings...")
        for ref_path in self.config.REFERENCE_PATHS:
            if not os.path.exists(ref_path):
                raise FileNotFoundError(f"Reference image not found: {ref_path}")

            for backend in self.config.DETECTOR_BACKENDS:
                try:
                    rep = DeepFace.represent(
                        img_path=ref_path,
                        model_name=self.config.MODEL_NAME,
                        detector_backend=backend,
                        enforce_detection=True
                    )
                    emb = np.array(rep[0]["embedding"]) if isinstance(rep, list) else np.array(rep["embedding"])
                    self.reference_embeddings.append(emb)
                    print(f"✅ Reference embedded with {backend}")
                    break
                except Exception as e:
                    print(f"⚠️ Backend {backend} failed: {e}")

        if not self.reference_embeddings:
            raise RuntimeError("No valid reference embeddings found.")

    def run_camera_verification(self):
        cap = cv2.VideoCapture(self.config.CAM_INDEX, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        counter, face_match, last_distance = 0, False, None
        print("Starting camera... Press 'q' to exit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Camera error.")
                break

            status_text = "MATCH" if face_match else "NO MATCH"
            color = (0, 255, 0) if face_match else (0, 0, 255)
            cv2.putText(frame, status_text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)

            if counter % self.config.FRAME_SKIP == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rep_probe = None

                for backend in [self.detector_backend_used] + [b for b in self.config.DETECTOR_BACKENDS if b != self.detector_backend_used]:
                    try:
                        rep_probe = DeepFace.represent(
                            img_path=frame_rgb,
                            model_name=self.config.MODEL_NAME,
                            detector_backend=backend,
                            enforce_detection=True
                        )
                        self.detector_backend_used = backend
                        break
                    except Exception:
                        continue

                if rep_probe:
                    probe_emb = np.array(rep_probe[0]["embedding"]) if isinstance(rep_probe, list) else np.array(rep_probe["embedding"])
                    distances = [cosine_distance(probe_emb, ref) for ref in self.reference_embeddings]
                    last_distance = min(distances)
                    face_match = last_distance <= self.config.COSINE_THRESHOLD
                else:
                    face_match = False

            if last_distance is not None:
                cv2.putText(frame, f"{last_distance:.3f}", (20, 420), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 0), 2)

            cv2.imshow("video", frame)
            counter += 1
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
