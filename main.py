from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Jadoo AI Oracle System is Running!"

def jadoo_thinking():
    while True:
        print("Jadoo is thinking and building system...")
        time.sleep(60)

if __name__ == "__main__":
    t = threading.Thread(target=jadoo_thinking)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=5000)
