from pypresence import Presence
import time

client_id = '' #Put your client ID here
RPC = Presence(client_id) 
RPC.connect() 

print(RPC.update(state="state here", details="details", large_image="large image", small_image="small image", large_text="text", start=time.time()))  # Set the presence

while True: 
    time.sleep(15) 