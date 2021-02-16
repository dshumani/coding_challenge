
from django.shortcuts import render,redirect




def index(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'index.html', {})
    elif request.method == "POST":
        if not request.session.exists(request.session.session_key):
            request.session.create()
            request.session.set_expiry(120)
            print("session key:", request.session.session_key)
        return render(request, "page_requiring_a_session.html")


def page_requiring_a_session(request, *args, **kwargs):
    if not request.session.exists(request.session.session_key):
        return render(request, 'access_denied.html', {})

    return render(request,"page_requiring_a_session.html")

def end_session(request,*args,**kwargs):
    request.session.flush()
    return redirect('index')

