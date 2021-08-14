# Exemplo de aplicativo Python que publica a Temperatura com MQTT Publish
# Link: https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

#Importação das Bibliotecas
import paho.mqtt.client as paho
from random import randrange, uniform
import time
import sys

# Localização do Broker
# mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "localhost"

# Identificando o Cliente 
client = paho.Client("Temperature_Inside")

# Conexão do Broker
if client.connect(mqttBroker, 8883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

# Loop da publicação da Temperatura
while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
