import paho.mqtt.client as mqtt
import json
import base64

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("v3/mpc-mks@ttn/devices/devkit-81/up")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    pld = json.loads(msg.payload.decode("utf-8"))
    string = base64.b64decode(pld["uplink_message"]["frm_payload"]).decode()
    print(string)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.username_pw_set("mpc-mks@ttn","NNSXS.B75L4YCIWKRIXUGEDS2NNGXTNAV4PHW7POSNS2Y.EE42KQNJKP36YCSLRH5SIU4I5XXC2KOQGJPIT3PRK4PKNMPDNIVQ")
mqttc.connect("eu1.cloud.thethings.network", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()