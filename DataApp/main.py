import os
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics','height','500')
Config.set('graphics','width','500')

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDIconButton, MDTextButton
from kivy.core.window import Window
from kivy.uix.image import Image

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('cat.kv')
	def GetImage(self):
		# assign directory
		imageDirectory = 'Pics'
		dirname = os.path.dirname(__file__)
		imageDirectory = os.path.join(dirname, imageDirectory)
		# iterate over files in
		# that directory
		list = os.listdir(imageDirectory)
		for filename in list:
			f = os.path.join(imageDirectory, filename)
			if os.path.isfile(f):
				print(filename)
class StartupWindow(Screen):
	pass


class MainWindow(Screen):
	pass

class RatingWindow(Screen):
	pass


class WindowManager(ScreenManager):
	pass


MainApp().run()