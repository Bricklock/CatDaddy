import os

from kivy.config import Config
from kivy.lang import Builder

Config.set('graphics','height','500')
Config.set('graphics','width','500')
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty

from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDTextButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.snackbar import Snackbar


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		self.currentImage = ""
		self.rated = []
		self.unrated = []
		return Builder.load_file('cat.kv')
	def GetImage(self):
		# assign directory
		imageDirectory = 'Pics'
		dirname = os.path.dirname(__file__)
		imageDirectory = os.path.join(dirname, imageDirectory)
		# get first unrated image
		self.unrated = os.listdir(imageDirectory)
		if len(self.unrated) != 0:
			imageString = os.path.join(imageDirectory, self.unrated.pop(0))
			if os.path.isfile(imageString):
				self.currentImage = imageString
				pass 
		else:
			Snackbar(text="Rated all images in file").show()
	def RateImage(self):
		self.GetImage()
		Image(source=self.currentImage, pos_hint = {"center_x": .5}, size_hint = (.9, .9))
		self.rated.append(self.currentImage)

class StartupWindow(Screen):
	pass

class MainWindow(Screen):
	pass

class RatingWindow(Screen):
		pass

class WindowManager(ScreenManager):
	pass

class RateSlider(MDBoxLayout):
	pass

class TestPause():
	def test():
		pass
	
MainApp().run()
