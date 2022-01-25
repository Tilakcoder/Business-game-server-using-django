from django.db import models


# Create your models here.
class Board(models.Model):
    board_name = models.CharField(max_length=30)
    player_amount = models.IntegerField()


class Players(models.Model):
    board_name = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
