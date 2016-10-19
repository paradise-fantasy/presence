import paho.mqtt.publish as publish

topic = "paradise/presence/data"


def send_presence_event(presence_event):
	data = str(presence_event)

	publish.single(topic, data, port=8883, tls={'ca_certs':"ca.crt",'tls_version':2}, hostname="nyx.bjornhaug.net")