from paho.mqtt import client as mqtt
from django.shortcuts import render
#from tkinter.filedialog import test


# Create your views here.

def connect(topic: str, playload: int):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client("client1")
    client.username_pw_set("guest", "guest")
    client.on_connect = on_connect
    client.connect("10.42.0.1", 1886)

    def on_publish(client, userdata, result):
        print("data published")
        pass

    client.on_publish = on_publish
    client.publish(topic=topic, payload=playload)


def index(request):
    return render(request, 'index.html')


def led_ON(request):
    connect(topic="lampe1", playload=0)
    etat = "allumée"
    return render(request, "prise_con/led1/LED1ON.html", {"e": etat})


def led_OFF(request):
    connect(topic="lampe1", playload=1)
    etat = "éteinte"
    return render(request, "prise_con/led1/led1OFF.html", {"e": etat})


def led(request):
    return render(request, "prise_con/led1/led1.html")
