# with redis
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from business.models import Board, Players


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message[1] == 'payment':
            raiser, e, him, amount, board_n = message
            b = Board.objects.get(board_name=board_n)
            p = Players.objects.get(board_name=b, name=raiser)
            p.amount = p.amount-amount
            p.save()
            r = Players.objects.get(board_name=b, name=him)
            r.amount = r.amount+amount
            r.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
