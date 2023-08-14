from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Welcome(request):
    return HttpResponse("""
                        <center><h1>Welcome to our Django app!</h1></center>
                        """)


def Greet(request,username):
    return HttpResponse(f"""         <center><h1>Hello {username}!</h1></center>""")


def Farewell(request,username):
   return HttpResponse(f"""         <center><h1>Bye Bye {username}!</h1></center>""")