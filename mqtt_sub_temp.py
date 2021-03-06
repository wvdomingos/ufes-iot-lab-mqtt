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
mqttBroker = "localhost"
client = paho.Client("Smartphone")
client.on_message = on_message

# Conexão do Broker
if client.connect(mqttBroker, 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.subscribe("TEMPERATURE")

try:
    print("Press CTRL+C to exit...")
    #client.loop_start()
    client.loop_forever()
    #time.sleep(30)
    #client.loop_end()
except:
    print("Disconnecting from broker")

client.disconnect()