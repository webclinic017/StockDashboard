from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
import json
from random import randint

class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(100):
            await self.send(json.dumps({'message': randint(1,100)}))
            await sleep(1) 