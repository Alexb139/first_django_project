from django.http import HttpResponse 

# Create your views here.

# def index(request) :
#     return HttpResponse('Hello, this is my first django app')

def index(request) :
    return HttpResponse(data)

data = {
    "Name": "Alexandria Baynes", 
    "Track": "Backend_(Python)", 
    "Message": "Thank_you_for_all_that_you_do!!"
}
 