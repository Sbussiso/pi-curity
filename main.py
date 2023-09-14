from camera import start_motion_detection
from video_manager import manage_videos

def main():
    while True:
        print("________________________________________________________")
        print("\nHome Security System")
        print("1. Arm (click on camera(s) and press escape to dissarm)")
        print("3. Video Manager")
        print("4. Exit")
        user_input = input("Enter choice: ")
        print("________________________________________________________")

        if user_input == "1":
            # Start monitoring and motion detection
            print("Security system armed. Monitoring for motion...")
            start_motion_detection() 

        elif user_input == "2":
            # Placeholder for disarming
            print("Functionality not yet implemented. You can press 'Esc' key when in the camera view to disarm for now.")
            
        elif user_input == "3":
            manage_videos()

        elif user_input == "4":
            print("Exiting...")
            break

        else:
            print("Unknown input!")

if __name__ == "__main__":
    main()
