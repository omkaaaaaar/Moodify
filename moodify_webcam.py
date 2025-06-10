import cv2
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(1)  # or 0 depending on working camera index

print("🎥 Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture frame")
        break

    try:
        # Analyze emotion (only on every few frames ideally, for speed)
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']

        # Show emotion on screen
        cv2.putText(frame, f'Emotion: {dominant_emotion}', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print("⚠️ Emotion detection failed:", e)

    # Display the video
    cv2.imshow("Moodify: Emotion Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
