"""Platzigram views"""
#ds: para escribir una respuesta en Django:
from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    """Return a gretting"""
    return HttpResponse(f"Hi! Current server time is {datetime.now().strftime('%b %dth, %Y - %H:%M hrs')}" )


def sort_integers(request):
    """Return a sorted list"""
    #import pdb; pdb.set_trace() #print(request)

    numbers = request.GET['numbers'].split(',')
    numbers = [int(n) for n in numbers]
    numbers_sorted = sorted(numbers)
    
    response = {
        'status' : 'ok',
        'numbers': numbers_sorted,
        'message' : 'Integers sorted successfully.'
    }

    return HttpResponse(
        json.dumps(response, indent=4), 
        content_type='application/json'
    )
    

def say_hi(request, name, age):
    """Return a greeting."""
    if age <= 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello, {name}! Welcome to Platzigram by DServo Labs'

    return HttpResponse(message)