from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from requests import get
import time
import kivy

Builder.load_file("main.kv")

class MyLayout(Widget):
	#START button
	def start_pressed_on(self):
		self.ids.button_start.bg_color=(1,0,0,1)
		self.ids.button_up.bg_color=(0,1,0,1)
		self.ids.button_down.bg_color=(0,1,0,1)
		self.ids.button_right.bg_color=(0,1,0,1)
		self.ids.button_left.bg_color=(0,1,0,1)
		self.ids.button_stop.bg_color=(0,1,0,1)
		self.ids.my_label.text= "starting!"
	def start_pressed_off(self):
		time.sleep(3)
		try:
			get("http://192.168.4.1/start")
		except:
			print("started!")
		self.ids.my_label.text= "started!"
		self.ids.button_start.bg_color=(0,1,0,1)
	#UP button
	def up_pressed_on(self):
		self.ids.button_up.bg_color=(1,0,0,1)
		self.ids.button_stop.bg_color=(0,1,0,1)
		self.ids.button_left.bg_color=(0,1,0,1)
		self.ids.button_right.bg_color=(0,1,0,1)
		self.ids.button_down.bg_color=(0,1,0,1)
	def up_pressed_off(self):
		self.ids.my_label.text= "Moving to the UP!"
		try:
			get("http://192.168.4.1/up")
		except:
			print("Moving to the UP!")
	#DOWN button
	def down_pressed_on(self):
		self.ids.button_down.bg_color=(1,0,0,1)
		self.ids.button_stop.bg_color=(0,1,0,1)
		self.ids.button_left.bg_color=(0,1,0,1)
		self.ids.button_right.bg_color=(0,1,0,1)
		self.ids.button_up.bg_color=(0,1,0,1)
	def down_pressed_off(self):
		self.ids.my_label.text= "Moving to the DOWN!"
		try:
			get("http://192.168.4.1/down")
		except:
			print("Moving to the DOWN!")
	#RIGHT button
	def right_pressed_on(self):
		self.ids.button_right.bg_color=(1,0,0,1)
		self.ids.button_stop.bg_color=(0,1,0,1)
		self.ids.button_left.bg_color=(0,1,0,1)
		self.ids.button_up.bg_color=(0,1,0,1)
		self.ids.button_down.bg_color=(0,1,0,1)
	def right_pressed_off(self):
		self.ids.my_label.text= "Moving to the RIGHT!"
		try:
			get("http://192.168.4.1/right")
		except:
			print("Moving to the RIGHT!")
	def left_pressed_on(self):
		self.ids.button_left.bg_color=(1,0,0,1)
		self.ids.button_stop.bg_color=(0,1,0,1)
		self.ids.button_right.bg_color=(0,1,0,1)
		self.ids.button_down.bg_color=(0,1,0,1)
		self.ids.button_up.bg_color=(0,1,0,1)
	def left_pressed_off(self):
		self.ids.my_label.text= "Moving to the LEFT!"
		try:
			get("http://192.168.4.1/left")
		except:
			print("Moving to the LEFT!")
	def stop_pressed_on(self):
		self.ids.my_label.text= "Cleaner just stoped!"
		self.ids.button_stop.bg_color=(1,0,0,1)
		self.ids.button_left.bg_color=(0,1,0,1)
		self.ids.button_right.bg_color=(0,1,0,1)
		self.ids.button_down.bg_color=(0,1,0,1)
		self.ids.button_up.bg_color=(0,1,0,1)
	def stop_pressed_off(self):
		time.sleep(0.5)
		self.ids.button_stop.bg_color=(0,1,0,1)
		try:
			get("http://192.168.4.1/stop")
		except:
			print("Cleaner just stoped!")
		
class VacuumCleaner(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	VacuumCleaner().run()