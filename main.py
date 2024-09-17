import asyncio
import websockets
import json

messages_json_file = 'messages.json'

async def sendduties(websocket):
    try:
        with open(messages_json_file, 'r') as f:
            duties = json.load(f)

        for duty in duties:
            await websocket.send(json.dumps(duty))
            print(f"Sent duty: {duty}")
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

async def main():
    async with websockets.serve(sendduties, "localhost", 8000):
        print("WebSocket server is running on ws://localhost:8000")
        await asyncio.Future()  # Run the server forever

if __name__ == "__main__":
    asyncio.run(main())