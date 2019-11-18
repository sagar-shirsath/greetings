from django.shortcuts import render
from webapp.models import Greetings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from greeetings.decortators import view_auth_classes



@view_auth_classes()
class GreetingsApp(APIView):
    def get(self,request):
        greeting = request.GET.get("greeting")
        if greeting:
            greetingobj = Greetings.objects.filter(title__startswith=greeting)
        else:
            greetingobj = Greetings.objects.filter().last()
        if greetingobj:
            greetingobj = greetingobj[0]
            return HttpResponse(json.dumps({'id':greetingobj.id,'title':greetingobj.title,'url':greetingobj.url, }),
                        status=200)
        else:
            return HttpResponse(json.dumps({}),
                        status=403)



def home(request):
    id =request.REQUEST.get("id")
    if id:
        greeting = Greetings.objects.get(id=id)
    else:
        greeting = Greetings.objects.filter().last()
    return render(request, 'home.html', {
        'greeting': greeting,
        'user' : request.user
    })

def login(request):
    if request.user.is_authenticated():
       return redirect("/home")

    return render(request, 'login.html', { })

