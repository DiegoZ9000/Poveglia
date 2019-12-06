from django.shortcuts import render_to_response


def index (request):
    return render_to_response('index.html')

def bio (request):
    return render_to_response('bio.html')

def links (request):
    return render_to_response('links.html')

def news (request):
    return render_to_response('news.html')
