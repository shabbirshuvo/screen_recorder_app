from kivy.clock import Clock
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp

from kivy.uix.button import Button
import cv2
import numpy as np
import pyautogui

from kivy.core.window import Window

Window.size = (450, 150)


class ScreenRecorder(MDApp):

    def __init__(self, **kwargs):
        super().__init__()
        self.record_button = None
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Using XVID codec
        self.output_file = 'screen_record.avi'
        self.fps = 30.0
        self.out = None
        self.screen_size = (int(pyautogui.size().width), int(pyautogui.size().height))
        self.recording = False

    def start_recording(self, event):
        if not self.recording:
            self.recording = True
            self.record_button.text = "Stop Recording"
            self.out = cv2.VideoWriter(self.output_file, self.fourcc, self.fps, self.screen_size)
            Clock.schedule_interval(self.record_screen, 1.0 / self.fps)
        else:
            self.recording = False
            self.record_button.text = "Record"
            Clock.unschedule(self.record_screen)
            if self.out:
                self.out.release()
                self.out = None

    def record_screen(self, dt):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.out.write(frame)

    def build(self):
        self.root = MDRelativeLayout(md_bg_color=(0, 0, 0, 1))
        self.record_button = Button(text="Record", size_hint=(0.8, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 0, 0, 1), bold=True, on_press=self.start_recording)
        self.root.add_widget(self.record_button)

        return self.root


if __name__ == '__main__':
    ScreenRecorder().run()
