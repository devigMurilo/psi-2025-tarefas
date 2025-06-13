from django.shortcuts import render

# Create your views here.
def index(request):
    usuarios = [
        ,{"nome":"michael douglas", "idade": 21, "matricula":1 "cidade": "sao tome"},
         {"nome":"michael douglas", "idade": 21, "matricula":1 "cidade": "sao tome"}
         {"nome":"michael douglas", "idade": 21, "matricula":1 "cidade": "sao tome"},
         {"nome":"michael douglas", "idade": 21, "matricula":1 "cidade": "sao tome"},
         {"nome":"michael douglas", "idade": 21, "matricula":1 "cidade": "sao tome"},
         {"nome":"michael douglas", "idade": 21, "matricula":1 "cidade": "sao tome"},]
    return render(request, usuarios, 'index.html')