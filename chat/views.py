from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, "chat/frontpage.html")