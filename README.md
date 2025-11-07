Abstract

This project focuses on creating a real-time face verification system that can recognize and confirm a person’s identity using a webcam. Instead of relying on passwords or cards, the system compares a live video feed with a stored reference image to decide if they belong to the same person. It uses ArcFace, a deep-learning model designed for facial recognition, and OpenCV to handle webcam input and display the results in real time. The main goal is to design a system that is easy to use, runs smoothly on normal hardware, and accurately identifies people even under normal day-to-day conditions. This concept can be applied to areas like attendance systems, login verification, and personal security.

Techstack

Category	                                                                         Tool Library	                                                                     Purpose                  
Programming Language	                                                             Python 3.x	                                                             Base language for development
IDE                                                                              	PyCharm                                                                	Used for coding and debugging
Computer Vision                                                                  	OpenCV	                                                                 Handles webcam and video frames
Deep Learning	                                                                    DeepFace (ArcFace)	                                                     Face embedding and recognition
Backend Engine	                                                                   TensorFlow / Keras	                                                     Runs the deep-learning model
Math Library                                                                     	NumPy	                                                                  Used for similarity and distance calculations
Version Control	                                                                  GitHub	                                                                 Stores and tracks project code
Environment	                                                                      Virtual Environment (.venv)	                                            Keeps dependencies isolated


Expected Output

When the program runs, a webcam window opens and detects the user’s face.
It shows live text feedback on the screen:
•	“MATCH” in green when the person matches the stored reference photo.
•	“NO MATCH” in red when the person is not recognized.
The system runs smoothly without needing a GPU or an internet connection.
It can be easily adapted for classroom attendance, secure logins, or door access verification.

Goals

The project’s main goals are:
1.	To design a real-time face verification system using deep learning and computer vision.
2.	To use ArcFace for generating highly accurate facial embeddings.
3.	To integrate OpenCV for live video capture and real-time feedback.

4.	4.	To make sure the system runs smoothly on a regular computer without a GPU.
5.	To structure the project in a way that makes it easy to upgrade with future features like multi-user access or liveness detection.

Requirements

Functional Requirements
•	Capture live video through a webcam.
•	Detect and align a face from each frame.
•	Compare the detected face to a reference image using ArcFace.
•	Display a live message — “MATCH” or “NO MATCH” — on the screen.
•	Allow the user to quit the program easily (e.g., by pressing “Q”).
Non-Functional Requirements
•	Should work efficiently on a standard CPU at around 10 frames per second.
•	Easy to install and run inside a virtual environment.
•	Should perform consistently in different lighting and moderate angles.
•	The codebase should be modular and simple to extend.

Hardware and Software Requirements

•	Hardware:
o	Laptop or PC with webcam
o	At least 4 GB RAM
o	Intel i5 or similar processor
•	Software:
o	Python 3.x
o	PyCharm IDE
o	Libraries: OpenCV, DeepFace (ArcFace), TensorFlow, NumPy

Risks and Limitations

Potential Risk	                                                    Impact                                                                     	Mitigation / Solution
Poor lighting or weak camera quality                              	May reduce accuracy	                                                      Test in good lighting and apply preprocessing if needed
Face partially covered (mask, glasses)                            	Might fail to detect correctly	                                           Add more reference images or improve model tuning
CPU-only execution	                                                Slight delay in processing	                                               Use frame skipping or lighter model variants
False positives/negatives	                                         Incorrect match result	                                                   Adjust similarity threshold through testing
No liveness detection	                                             Risk of spoofing with a photo	                                            Add blink/motion detection in future
Library version issues	                                            Installation errors                                                      	Use fixed versions in requirements.txt
These risks are normal for early-stage machine learning projects, but most can be managed through careful testing and model optimization.




