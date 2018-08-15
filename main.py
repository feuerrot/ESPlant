import mqtt
import network
import max7219
import moisture
import timer
import time
import machine

def init_wifi():
	nic = network.WLAN(network.STA_IF)
	nic.active(True)
	nic.connect("CCCAC_PSK_2.4GHz", "23cccac42")

	while not nic.isconnected():
		time.sleep_ms(100)
	print("WIFI connection established")

def init_mqtt(mqtt):
	mqtt.connect()
	print("MQTT connection established")

def publish_plant(sensor):
	m.publish("sensors/plant/{}".format(sensor.name), str(sensor.result))
	print("PLANT {} VALUE {}".format(sensor.name, sensor.result))
	display.write_string("  {: >4}  ".format(sensor.result))

def add_plant():
	sensor.set_timer()
	tmr.add(10 * 1000, add_plant)

print("Boot complete")
m = mqtt.MQTTClient("Pflanze_{}".format(machine.unique_id()), "mqtt.space.aachen.ccc.de")
display = max7219.max7219()
display.clear()

tmr = timer.Timer(50)

sensor = moisture.Moisture("alpha", 36, 1000, 5, publish_plant, tmr)

init_wifi()
init_mqtt(m)

add_plant()
tmr._start()
