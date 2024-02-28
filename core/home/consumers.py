from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_group_consumer'
        async_to_sync(self.channel_layer.group_add)(
            # self.room_name, # by room name
            self.room_group_name,
            self.channel_name, # by channel name. access from model/view/other
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'Connected from Django Channel'}))

    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps(text_data))

    def disconnect(self, *args, **kwargs):
        print('Disconnected')

    def send_notification(self, event):
        print(event.get('value'))
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))

