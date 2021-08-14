#!/usr/bin/python

# Exemplo de aplicativo Python que publica a Temperatura com MQTT Publish
# Link: https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

#Importação das Bibliotecas
import thread
import paho.mqtt.client as paho
from random import randrange, uniform
import time
import sys

# Localização do Broker
# mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "localhost"

# Função para publicação da Temperatura do IoT
def pub_temp(threadName, delay):
    # Identificando o Cliente 
    client = paho.Client("IoT01")

    # Conexão do Broker
    if client.connect(mqttBroker, 8883, 60) != 0:
        print("Could not connect to MQTT Broker!")
        sys.exit(-1)

    # Loop para a publicação da Temperatura do IoT
    while True:
        randNumber = uniform(20.0, 21.0)
        client.publish("IoT/Temperatura", randNumber)
        print("Temperatura: " + str(randNumber) + " para Topico IoT/Temperatura")
        time.sleep(delay)

# Create two threads as follows
try:
   thread.start_new_thread( pub_temp, ("Thread-1", 2, ) )
   thread.start_new_thread( pub_temp, ("Thread-2", 4, ) )
except:
   print("Error: unable to start thread")

