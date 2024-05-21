from django.http import HttpRequest
from django.shortcuts import render

def render_to_do(request: HttpRequest):
  return render(request, 'page.html')

