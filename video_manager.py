import cv2
import os

def manage_videos():
    while True:
        def play_video(video_path):
            # Open the video file.
            cap = cv2.VideoCapture(video_path)
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                cv2.imshow('Video Playback', frame)

                # Close the video file when 'q' key is pressed
                if cv2.waitKey(40) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()


        def list_videos(directory):
            return [f for f in os.listdir(directory) if f.endswith('.avi')]

        def view_camera():
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Error: Could not open camera!")
                return
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                cv2.imshow('Live Camera Feed', frame)
                
                # Close the live feed when 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        print('1. View security footage')
        print('2. Delete footage')
        print('3. View camera')
        print('4. Exit')
            
        user_input = input("Enter choice: ")
            
        if user_input == '1':
            video_files = list_videos('Security Snapshots')
            if not video_files:
                print("No videos found!")
                continue

            print("\nAvailable videos:")
            for idx, vid in enumerate(video_files, start=1):
                print(f"{idx}. {vid}")
                
            choice = input("\nEnter the number of the video you want to play: ")
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(video_files):
                    play_video(os.path.join('Security Snapshots', video_files[choice_idx]))
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number.")

        elif user_input == '2':
            video_files = list_videos('Security Snapshots')
            if not video_files:
                print("No videos found!")
                continue

            print("\nAvailable videos:")
            for idx, vid in enumerate(video_files, start=1):
                print(f"{idx}. {vid}")

            choice = input("\nEnter the number of the video you want to delete or type 'delete all' to delete all videos: ")

            if choice.lower() == 'delete all':
                confirm = input(f"Are you sure you want to delete all videos? (yes/no) ")
                if confirm.lower() == 'yes':
                    for vid in video_files:
                        os.remove(os.path.join('Security Snapshots', vid))
                    print("All videos deleted successfully!")
                else:
                    print("Delete operation cancelled.")
                continue

            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(video_files):
                    confirm = input(f"Are you sure you want to delete {video_files[choice_idx]}? (yes/no) ")
                    if confirm.lower() == 'yes':
                        os.remove(os.path.join('Security Snapshots', video_files[choice_idx]))
                        print("Video deleted successfully!")
                    else:
                        print("Delete operation cancelled.")
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number.")


        elif user_input == '3':
            print("press q to quit live camera feed")
            view_camera()
            
        elif user_input == "4":
            break

        else:
            print("Unknown input!")
