import os 
from opcua import Client
import time
import socket 

print("here!")

host = os.getenv("HOST") or "opc.tcp://0.0.0.0:4840/freeopcua/server/"
client = Client(host)
client.connect()

temperature_data = client.get_node("ns=2;i=2")
time_data = client.get_node("ns=2;i=3")

print("Client has Started!")
while True:
    print(f"Temperature Data: {temperature_data.get_value()}")
    print(f"Time: {time_data.get_value()}")
    time.sleep(2)