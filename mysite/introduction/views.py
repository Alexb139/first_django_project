from django.http import HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse(data)

data = {
    "Name": "Alexandria Baynes",
    "Track": "Backend (Python)",
    "Message": "Thank you for all that you do!!"
}