import mqtt
import network
import moisture
import timer
import time
import machine
import ubinascii

UID = ubinascii.hexlify(machine.unique_id()).decode()

def init_wifi():
	nic = network.WLAN(network.STA_IF)
	nic.active(True)
	nic.connect("CCCAC_OPEN_2.4GHz", None)

	while not nic.isconnected():
		time.sleep_ms(100)
	print("WIFI connection established")

def init_mqtt(mqtt):
	mqtt.connect()
	print("MQTT connection established")

def publish_plant(sensor):
	m.publish("sensors/plant/{}/{}".format(UID, sensor.name), str(sensor.result))
	print("PLANT {} VALUE {}".format(sensor.name, sensor.result))

def add_plant():
	for s in sensor:
		s.set_timer()
	tmr.add(10 * 1000, add_plant)

print("Boot complete")
m = mqtt.MQTTClient("Pflanze_{}".format(UID), "mqtt.space.aachen.ccc.de")

tmr = timer.Timer(50)

sensor = [
	moisture.Moisture("alpha", 36, 1000, 5, publish_plant, tmr),
	moisture.Moisture("beta",  39, 1000, 5, publish_plant, tmr),
	moisture.Moisture("gamma", 34, 1000, 5, publish_plant, tmr),
	moisture.Moisture("delta", 35, 1000, 5, publish_plant, tmr)
]


init_wifi()
init_mqtt(m)

add_plant()
tmr._start()
