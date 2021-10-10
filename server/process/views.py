import os
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        os.system('python3 process_data.py')
        return JsonResponse({'token': 'updated'})

    if 'output.csv' in os.listdir('..'):
        df = pd.read_csv('../output.csv')
        df = df.to_json()
        return JsonResponse({'token': df })
    return JsonResponse({'token': 'no data yet!'})
