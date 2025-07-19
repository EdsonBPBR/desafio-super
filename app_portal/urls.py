from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagamentos/pix/', views.gerar_pix, name='gerar_pix'),
]
