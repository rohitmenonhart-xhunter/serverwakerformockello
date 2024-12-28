import requests
import time
import os

def ping_server():
    url = "https://serverforpaymentmockello.onrender.com/ping"
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Server is up and running!")
            else:
                print(f"Failed to ping the server. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error pinging server: {e}")

        time.sleep(30)  # Wait for 30 seconds before pinging again


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    ping_server()
