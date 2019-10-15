from django.shortcuts import render

# Create your views here.

def home_view(request):
    if request.user.is_authenticated():
        context ={
            'name':'Orxan'
        }
    else:
        context = {
            'name':'Guest'
        }
    return render(request,'home.html', context)