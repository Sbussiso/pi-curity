import cv2
import datetime
import os
import sys
import threading
from notifications import send_sms_via_twilio

def start_motion_detection():
    def notify_user():
        send_sms_via_twilio("Motion detected by security camera!", "3602806070")

    SAVE_PATH = "Security Snapshots"
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    # Select codec based on OS
    if sys.platform == "darwin":  # macOS
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    else:  # Windows and other platforms
        fourcc = cv2.VideoWriter_fourcc(*'XVID')

    video_writer = None
    motion_frames_count = 0

    last_sms_time = datetime.datetime.now() - datetime.timedelta(minutes=5)  # Initialize to 5 mins ago

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 900:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            motion_detected = True

        if motion_detected:
            if video_writer is None:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                video_filename = os.path.join(SAVE_PATH, f"motion_detected_{timestamp}.avi")
                video_writer = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
            
            video_writer.write(frame1)
            motion_frames_count = 0
            
            # Check the time since the last SMS was sent
            now = datetime.datetime.now()
            time_since_last_sms = (now - last_sms_time).total_seconds()
            if time_since_last_sms > 300:  # e.g., 5 minutes = 300 seconds
                threading.Thread(target=notify_user).start()  # Start a new thread to send the SMS
                last_sms_time = now
            
        else:
            motion_frames_count += 1
            if motion_frames_count >= 100:  # no motion for 100 frames, stop recording
                if video_writer is not None:
                    video_writer.release()
                    video_writer = None
                motion_frames_count = 0

        cv2.imshow("Feed", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(40) == 27:  # Esc key to exit
            break

    if video_writer is not None:
        video_writer.release()

    cv2.destroyAllWindows()
    cap.release()

# If you have other parts of your code, add them below this.
