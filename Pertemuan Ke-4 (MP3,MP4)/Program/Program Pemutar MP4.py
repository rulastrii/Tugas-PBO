'''
Nama    : Rulastri
Kelas   : TI22L
NIM     : 220511071
'''

import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        # Create a VideoCapture object
        self.cap = cv2.VideoCapture()

        # Create a label to display the video frames
        self.label = tk.Label(root)
        self.label.pack(padx=10, pady=10)

        # Create buttons
        self.btn_open = tk.Button(root, text="Open Video", bg='yellow', fg='black', command=self.open_video)
        self.btn_open.pack(pady=5)

        self.btn_play = tk.Button(root, text="Play", bg='blue', fg='white', command=self.play_video)
        self.btn_play.pack(pady=5)

        self.btn_stop = tk.Button(root, text="Stop", bg='grey', fg='white', command=self.stop_video)
        self.btn_stop.pack(pady=5)

        self.btn_exit = tk.Button(root, text="Exit", bg='red', fg='white', command=root.destroy)
        self.btn_exit.pack(pady=5)

        
    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        if file_path:
            self.cap.open(file_path)

            # Get the video's width and height
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Resize the window to match the video resolution
            self.root.geometry(f"{width}x{height}")

    def play_video(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Convert the frame to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to ImageTk format
                img = Image.fromarray(rgb_frame)
                img_tk = ImageTk.PhotoImage(img)

                # Update the label with the new frame
                self.label.img_tk = img_tk
                self.label.config(image=img_tk)
                self.root.update()

                # Pause for a short time (approximately 33 milliseconds for 30 fps)
                self.root.after(10, self.play_video)(33)

                # Press Q on the keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

    def stop_video(self):
        # Release the video capture object
        self.cap.release()
        # Close the OpenCV window
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
