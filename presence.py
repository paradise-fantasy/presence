#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from bluetooth_handler import check_home
from mqtt_api import send_presence_event send_everyone_present



havard		=	Person("Haavard",		"40:B8:37:2C:C6:9F", 	"blue")
frederik	=	Person("Frederik",		"18:65:90:49:90:6C",	"green")
raymi		=	Person("Raymi",			"84:8E:DF:4B:D7:9F",	"red")
tormod		=	Person("Tormod",		"F4:8E:92:7F:27:12",	"yellow")
kabbe		=	Person("Jon-Anders",	"08:21:EF:7A:E7:88",	"cyan")


list_of_members = [havard, frederik, raymi, tormod, kabbe]
currently_home = 0

def main():
	print("[*] Paradise: Who's home?")
	while True:

		for person in list_of_members:
			check_home(person)
		counter = 0
		for deltager in list_of_members:
			if deltager.isPresent()
				counter += 1
		if (counter == 4 && currently_home != 4):
			send_everyone_present("true")
		else if (currently_home != 4)
			currently_home = counter

		time.sleep(2)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("[*] Shutting down.")
