from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
import json
from random import randint
from stocks import alpaca, func
import yfinance as yf

class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'stock_data'
        
        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        # for i in range(100):
        #     await self.send(json.dumps({'message': randint(1,100)}))
        #     await sleep(1) 
    
    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket (JS frontend)
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data_mode = text_data_json['data_mode']
        stock_select = text_data_json['stock_select']

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'stock_message',
                'data_mode': data_mode,
                'stock_select': stock_select,
            }
        )
    
    # Receive message from group
    async def stock_message(self, event):
        data_mode = event['data_mode']
        stock_select = event['stock_select']
        market_open = alpaca.isOpen()
        x_val, y_val = func.getHistorical(stock_select,data_mode)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'market_open': market_open,
            'x_val': x_val,
            'y_val': y_val,
        }))