import json
from django.http import JsonResponse

# Create your views here.

def index(request) :
    return JsonResponse(json.dumps(data))

data = {
    "Name": "Alexandria Baynes",
    "Track": "Backend (Python)",
    "Message": "Thank you for all that you do!!"
}