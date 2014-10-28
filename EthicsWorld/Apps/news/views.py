from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.forum.models import Issue, Responses

def index(request):
    return render(request, 'newsindex.html')
