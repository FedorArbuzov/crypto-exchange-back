import json

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from deals.models import Orders
from deals.utils.get_exchanges import get_exchange_rate



def exchanges(request):
    return JsonResponse(get_exchange_rate())


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Orders(
            order_id=data['order_id'],
            email=data['email'],
            phone=data['phone'],
            currensy=data['currensy'],
            operation=data['operation'],
            amount_give=data['amount_give'],
            amount_get=data['amount_get'],
            where_send_money=data['where_send_money']
        )
        order.save()
        return JsonResponse({'message': 'Order created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)