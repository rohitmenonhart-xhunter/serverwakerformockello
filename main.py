from flask import Flask
import requests
import time
import threading
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "Pong!", 200

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
    # Start the ping_server function in a separate thread
    threading.Thread(target=ping_server, daemon=True).start()

    # Start the Flask server on the port specified by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
