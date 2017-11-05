# -*- coding: utf-8 -*-

# Copyright 2008-2017 Jaap Karssenberg <jaap.karssenberg@gmail.com>


class NavigationModel(object):
	'''This class defines an object that decides how and where to open
	pages, files and other objects in the user interface.
	'''

	def __init__(self, window):
		self.window = window

	def open_page(self, path, new_window=False):
		if new_window:
			self.window.ui.open_new_window(path) # XXX
		else:
			self.window.open_page(path)

		return self.window.pageview