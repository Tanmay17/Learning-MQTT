import paho.mqtt.client as mqtt
import time

# broker_address = "192.168.1.103"
broker_address = "iot.eclipse.org"

def on_connect(client, userData, flags, rc):
    print "connected with result code"+str(rc)
    client.subscribe('$SYS/#')

# print "Publishing the message to topic" , "house/bulbs/bulb1"
# client.publish("I'm publishing, don't know what")

def on_message(client, userdata, message):
    print "message recieved", str(message.payload.decode("utf-8"))
    print "message topic=", message.topic
    print "message qos=", message.qos
    print "message retain flag=", message.retain

print "Creating new instance"
client = mqtt.Client(client_id="iam_10may", clean_session=True, userdata=None, transport="tcp")
# client.on_connect = on_connect
client.on_message = on_message  
print "connecting to broker"
client.connect(broker_address, 1883, 600)
client.loop_start()
print "Subscribing to the topic", "house/bulbs/bulb1"
client.subscribe("house/bulbs/bulb1")
print "Publishing to the topic", "house/bulbs/bulb1"
client.publish("house/bulbs/bulb1", "OFF")
time.sleep(4)
# client.loop_forever()
client.loop_stop()