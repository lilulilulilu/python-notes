# client.py
# pip install websocket-client
import websocket
import threading
import time

def on_message(_, message):
    print("Received: %s" % message)

def on_error(_, error):
    print("Error: %s" % error)

def on_close(_):
    print("### closed ###")

def on_open(ws):
    def run():
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("Thread terminating...")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8765/hello",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()