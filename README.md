# pi-curity

This is a home security system built using a raspberry pi and a usb camera.

This project uses OpenCV to detect motion and record video footage when it is detected. The video is then stored localy in the directory and accessed thru the video manager. It will then notify the user(s) thru an SMS message.

Thru the video manager you can:
- view security footage
- delete security footage
- view camera for positioning


# pi-curity overview

pi-curity is a homegrown home security system designed with utmost regard for privacy and data integrity. Unlike many commercial security systems that have been caught violating user privacy, pi-curity ensures all data remains local, removing any possibility of unauthorized backdoor access.

# Technologies

**Hardware:**

USB Camera, Raspberry Pi 4 B

**Backend:**

Flask (Python)

**Frontend:**

HTML, CSS, JavaScript

**Motion Detection:** 

OpenCV

**Notification System:** 

Twilio for SMS notifications

# Features

Local Data Storage: Ensures maximum privacy by keeping all recorded data on your premises.

Motion Detection & Recording: Utilizes AI via OpenCV to detect any motion and commences recording once detected.

Instant Notifications: Stay updated about any activity. When motion is detected, receive prompt SMS notifications through Twilio.

Web Interface: Arm or disarm the security system, watch live camera feeds, or view recorded videos at your convenience, all through a user-friendly web application.

# Usage

Upon setting up the hardware components, simply navigate to the pi-curity web app using any device with an internet connection. The intuitive interface provides easy access to all functionalities, allowing users to manage their home security with ease.
Contributing

pi-curity is a free and open-source initiative. The community is encouraged to contribute, further enhancing its features, refining the AI, or adding new functionalities. Before making a pull request, it would be beneficial to check any contribution guidelines (if available).
License

pi-curity is released under an open-source license. This means everyone is free to copy, modify, or implement it in their projects without any restrictions.
