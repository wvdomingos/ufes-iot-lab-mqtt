# Exemplo de aplicativo Python que assina a Temperatura com MQTT Subscribe
# Link: https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

#Importação das Bibliotecas
import paho.mqtt.client as paho
import time
import sys

# Função que recebe a mensagem
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

# Localização do Broker
# mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "'localhost', 1883, 60"
client = mqtt.Client("Smartphone")

# Conexão do Broker
if client.connect(mqttBroker) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_end()