from kivy.clock import Clock
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp

from kivy.uix.button import Button
from kivy.uix.label import Label
import cv2
import numpy as np
import pyautogui

from kivy.core.window import Window

Window.size = (450, 150)


class ScreenRecorder(MDApp):

    def start_recording(self, instance):
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.output_file = 'output.mp4'
        self.fps = 30.0
        self.out = None
        self.screen_size = (1920, 1080)

    def build(self):
        self.root = MDRelativeLayout(md_bg_color=(0, 0, 0, 1))
        self.record_button = Button(text="Record", size_hint=(0.8, None), pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 0, 0, 1), bold=True, on_press=self.start_recording)
        self.root.add_widget(self.record_button)

        return self.root


if __name__ == '__main__':
    ScreenRecorder().run()
