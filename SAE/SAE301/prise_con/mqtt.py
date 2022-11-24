from django.shortcuts import render
import paho.mqtt.client as mqtt
import ssl
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

mytransport = 'tcp'

client = mqtt.Client(client_id="test",
        transport=mytransport,
        protocol=mqtt.MQTTv5)

client.username_pw_set("guest", "guest")
client.tls_set(certfile=None,
               keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED)

broker = '10.42.0.1'
myport = 1886
properties=Properties(PacketTypes.CONNECT)
properties.SessionExpiryInterval= 30*60 # in seconds


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/lampe")
    client.subscribe("/lampe1")


def on_message(client, userdata, msg):
    print(msg.topic+""+str(msg.payload))
    
def on_publish(client, userdata, result):
    print("data published")
    pass


client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect(broker,
       port=myport,
       clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY,
       properties=properties,
       keepalive=60)