#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person:
	def __init__(self, name, bluetooth_address, color):
		self.bluetoothPresence = False
		self.name = name
		self.bluetooth_address = bluetooth_address
		self.color = color

	def isPresent(self):
		return self.bluetoothPresence
	def setPresence(self, presence):
		self.bluetoothPresence = presence
	def getColor(self):
		return self.color
