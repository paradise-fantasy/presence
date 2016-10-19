#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from termcolor import colored
from mqtt_api import send_presence_event


def check_home(person):
	result = bluetooth.lookup_name(person.bluetooth_address, timeout=5)
	if (result != None):
		if not (person.isPresent()):
			print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + "  " + colored(person.name, person.getColor()) + " har ankommet!")
			send_presence_event(str(str(person.name) + " har ankommet!"))
			person.setPresence(True)

	elif ( person.isPresent() ) :
		print( time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) +"  " + colored(person.name, person.getColor()) + " har dratt.")
		send_presence_event(str(str(person.name) + " har dratt!"))
		person.setPresence(False)
