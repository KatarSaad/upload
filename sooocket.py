import websockets
import asyncio

import cv2, base64

print("Started server on port : ", 5000)


async def transmit(websocket, path):
    print("Client Connected !")
    try:
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            _, frame = cap.read()

            encoded = cv2.imencode('.jpg', frame)[1]

            data = str(base64.b64encode(encoded))
            data = data[2:len(data) - 1]

            await websocket.send(data)

            cv2.imshow("Transimission", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except websockets.connection.ConnectionClosed as e:
        print("Client Disconnected !")


start_server = websockets.serve(transmit, port=5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()