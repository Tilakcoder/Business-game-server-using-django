from django.shortcuts import render
from business.models import Board, Players
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your views here.
def index(r):
    return render(r, 'business/index.html')


def redirect(r):
    board_nam = r.GET['name']
    player_name = r.GET['playern']
    get = len(Board.objects.filter(board_name=board_nam))
    print(get)
    if get == 1:
        print("Already here")
        board_n = Board.objects.get(board_name=board_nam)
        ch_p = Players.objects.filter(board_name=board_n, name=player_name)
        if len(ch_p) == 0:
            player_n = Players(board_name=board_n, name=player_name, amount=board_n.player_amount)
            player_n.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "chat_"+board_nam,
                {
                    'type': "chat_message",
                    'message': [player_name, 'New_player', board_n.player_amount]
                }
            )
        else:
            player_n = ch_p[0]
        all_ps = Players.objects.filter(board_name=board_n)
        return render(r, 'business/dashboard.html', {"board_name": board_nam, "Player_name": player_n.name,
                                                     "Amount": player_n.amount, "all_ps": all_ps})
    else:
        return render(r, 'business/create.html', {"board_name": board_nam})


def make_board(r, room_name):
    starter = r.GET['starter']
    bank_starter = r.GET['bank_amount']
    get = len(Board.objects.filter(board_name=room_name))
    if get == 0:
        b = Board(board_name=room_name, player_amount=starter)
        p = Players(board_name=b, name='Bank', amount=bank_starter)
        b.save()
        p.save()
    else:
        b = Board.objects.get(board_name=room_name)
        p = Players.objects.get(board_name=b, name='Bank')
    all_ps = Players.objects.filter(board_name=b)
    return render(r, 'business/dashboard.html', {"board_name": room_name, "Player_name": 'Bank', "Amount": p.amount,
                                                 "all_ps": all_ps})


def dashboard(r):
    return render(r, 'business.dashboard.html')
