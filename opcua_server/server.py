import time
import os 
import pdb 
import random
from opcua import ua, Server
import datetime

host = os.getenv("SERVER") or 'opc.tcp://192.168.25.26:4840/freeopcua/server/' 
server = Server()
server.set_endpoint(host)

# setup our own namespace, not really necessary but should as spec
uri = "OPCUA Server"
idx = server.register_namespace(uri)
# get Objects node, this is where we should put our nodes
node = server.get_objects_node()
params = node.add_object(idx, "data")

Temperature = params.add_variable(idx,"Temperature", 0)
Time = params.add_variable(idx,"Time",0)

Temperature.set_writable()
Time.set_writable()

server.start()

print("Server started")

while True:

    temp_value = random.uniform(-50, 50)
    t_value = datetime.datetime.now()
    Temperature.set_value(temp_value)
    Time.set_value(t_value) 

    time.sleep(1)

