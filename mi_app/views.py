from django.shortcuts import render

from django.http import HttpResponse

from mi_app.models import Familiares



def listar_familiares(request):

    context = {
        "familiares": Familiares.objects.all(),
    }
    return render(request, "mi_app/familiares.html", context)