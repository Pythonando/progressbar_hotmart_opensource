from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Batch, SalesTicket
from django.db import transaction

def progressbar(request, offer_code):
    batch = get_object_or_404(Batch, offer_code=offer_code)
    percentual = (batch.tickets_sales * 100) / batch.total_tickets
    return JsonResponse({'progress': int(percentual)})



@csrf_exempt
def webhook_hotmart(request):
    
    token = request.headers.get('X-Hotmart-Hottok')
    if token != settings.HOTTOK:
        print('token inválido')
        return HttpResponse('Token inválido')
    print(1)
    payload = json.loads(request.body)

    product_id = payload['data']['product']['id']
    print(2)
    if payload['data']['purchase']['status'] in {'APPROVED', 'COMPLETED'}:
        if int(product_id) == int(settings.PRODUCT_ID):

            batch = Batch.objects.get(offer_code=payload['data']['purchase']['offer']['code'])
            batch.tickets_sales += 1
            
            with transaction.atomic():
                SalesTicket.objects.get_or_create(
                    email=payload['data']['buyer']['email'],
                    defaults={
                        'telefone': payload['data']['buyer']['checkout_phone'],
                        'name': payload['data']['buyer']['name'],
                        'batch': batch
                    }

                )
                batch.save()

    return HttpResponse()