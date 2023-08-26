from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def setor(request):
    return render(request, 'setor.html')

def logout(request):
    return render(request, 'logout.html')

