from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Titre': 'Dashboard',

    }

    return render(request,'dashboard/index.html',context)