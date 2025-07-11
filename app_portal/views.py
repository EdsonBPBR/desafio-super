from django.shortcuts import render

#era uma boa definir o nome das funções em portugues
def home(request):
    return render(request, 'app_portal/home.html')
