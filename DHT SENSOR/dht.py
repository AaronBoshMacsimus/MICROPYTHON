import dht
import machine
import time
dht_sensor = dht.DHT11(machine.Pin(2))#CHANGE PIN ACCORDINGLY 
while True:
    try:
        dht_sensor.measure()
        temperature_celsius = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print("Temperature: {}°C, Humidity: {}%".format(temperature_celsius, humidity))
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
