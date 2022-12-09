import requests
import time

server_address = input("Enter the address of the Minecraft server you want to check: ")

while True:
    response = requests.get(f"https://api.mcsrvstat.us/2/{server_address}")

    if response.status_code == 200:
        data = response.json()
        if data["online"]:
            print(f"Pinging {server_address}")
            print("Server is online")
            print(f"Player count: {data['players']['online']} / {data['players']['max']}")
            with open("server_status.txt", "w") as f:
                f.write(f"Server IP: {server_address}\n")
                f.write(f"Player count: {data['players']['online']} / {data['players']['max']}\n")
                f.write("Server is online")
        else:
            print(f"Pinging {server_address}")
            print("Server is offline")
            with open("server_status.txt", "w") as f:
                f.write(f"Server IP: {server_address}\n")
                f.write("Server is offline")
    else:
        print("Failed to get server status :(")

    time.sleep(5)
