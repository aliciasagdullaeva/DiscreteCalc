"""DiscreteCalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from main import views
from DiscreteCalc import settings

urlpatterns = [
    path('', views.index, name='main'),
    path('admin/', admin.site.urls),
    path('encode/', views.encode, name='encode'),
    path('logic/', views.logic, name='logic'),
    path('huffman/', views.HuffmanView.as_view(), name='huffman'),
    path('hamming/', views.HammingView.as_view(), name='hamming'),
    path('TDNF/', views.TDNFView.as_view(), name='TDNF'),
    path('equality/', views.equality, name='equality'),
    path('monotone/', views.monotone, name='monotone'),
    path('self-duality/', views.self_duality, name='self_duality'),
    path('sheff/', views.sheff, name='sheff'),
    path('polynom/', views.polynom, name='polynom')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
