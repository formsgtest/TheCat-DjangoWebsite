from django.shortcuts import render

def index(request):
    context = {
        "title": "The Cat !!",
    }
    return render(request, "index.html", context)

