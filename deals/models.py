from django.db import models
from django.utils.timezone import now

# Create your models here.

CURRENCY_CHOICES = (
    ('btc','BTC'),
    ('usdt', 'USDT'),
)

OPERATION_CHOICES = (
    ('buy','BUY'),
    ('sell', 'SELL'),
)

class Orders(models.Model):
    order_id = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    currensy = models.CharField(max_length=6, choices=CURRENCY_CHOICES, default='usdt')
    operation = models.CharField(max_length=6, choices=OPERATION_CHOICES, default='buy')
    amount_give = models.IntegerField()
    amount_get = models.IntegerField()
    where_send_money = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now, editable=False)