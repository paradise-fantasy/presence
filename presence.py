#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluetooth
import time
from Person import Person
from bluetooth_handler import check_home


havard		=	Person("Haavard",		"40:B8:37:2C:C6:9F", 	"blue")
frederik	=	Person("Frederik",		"18:65:90:49:90:6C",	"green")
raymi		=	Person("Raymi",			"84:8E:DF:4B:D7:9F",	"red")
tormod		=	Person("Tormod",		"F4:8E:92:7F:27:12",	"yellow")
kabbe		=	Person("Jon-Anders",	"F4:8E:92:7F:27:10",	"cyan")


list_of_members = [havard, frederik, raymi, tormod, kabbe]

def main():
	print("[*] Paradise: Who's home?")
	while True:

		for person in list_of_members:
			check_home(person)

		time.sleep(2)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("[*] Shutting down.")
