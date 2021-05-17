from django.http import JsonResponse 

# Create your views here.

# def index(request) :
#     return HttpResponse('Hello, this is my first django app')

def index(request) :
    return JsonResponse(data)

data = {
    "Name": "Alexandria Baynes", 
    "Track": "Backend_(Python)", 
    "Message": "Thank_you_for_all_that_you_do!!"
}
 