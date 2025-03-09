from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
import os
from django.shortcuts import render
from django.http import HttpResponse

def serve_react_app(request):
    index_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "dist", "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            return HttpResponse(f.read())
    else:
        return HttpResponse("React build not found. Run `npm run build` inside frontend/", status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', serve_react_app),  # Serve React frontend
]
