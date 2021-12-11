import time
import websockets
import asyncio
import json

async def inp():
    url = "wss://stream.binance.com:9443/stream?streams=ethusdt@miniTicker"
    async with websockets.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']
            #время транзакции
            time_well = time.localtime(data['E'] // 1000)
            #rурс по $
            well = data['c']
            print(time_well, well)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(inp())
