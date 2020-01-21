from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader


from .models import New



def index (request):
    latest_news_list = New.objects.order_by('published_date')[:5]
    output = ', '.join([n.text for n in latest_news_list])
    template = loader.get_template('index.html')
    context = {
        'latest_news_list': latest_news_list,
        'clave': 'valor'
    }
    return HttpResponse(template.render(context, request))


def bio (request):
    return render_to_response('bio.html')

def vids (request):
    return render_to_response('vids.html')
