from django.shortcuts import render, redirect

from django.views.generic.base import RedirectView

# Create your views here.



def resume(request):
    return render(request, "resume.html")

def mastodon_redirect(request):
    return redirect("https://its.bencarneiro.com/@ben")


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)