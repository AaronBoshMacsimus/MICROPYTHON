import network
from umqtt.robust import MQTTClient
from umqtt.simple import MQTTClient
import machine
import time
ssid = "FILL HERE"
password = "FILL HERE"
aio_username = "FILL HERE"
aio_key = "FILL HERE"
aio_feed = "FILL HERE"
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to Wi-Fi...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("Connected to Wi-Fi")
def send_data(data):
    c = MQTTClient("FILL HERE", "io.adafruit.com", user=aio_username, password=aio_key)
    c.connect()
    topic = f"{aio_username}/feeds/{aio_feed}"
    c.publish(topic, data)
    c.disconnect()
connect_wifi()
while True:
    data_to_send = sen("HELLO")
    send_data(data_to_send)
