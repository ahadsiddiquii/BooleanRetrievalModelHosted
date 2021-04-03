from django.shortcuts import render,HttpResponse

# Create your views here.
def renderHome(request):
    return render(request,'home.html')
    # return HttpResponse('home page rendered')