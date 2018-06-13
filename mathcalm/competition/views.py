from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.http import require_GET

from .models import Competition
# Create your views here.

@require_GET
def main(request):

    return HttpResponse()


@require_GET
def competitions(request):

    comp_list = Competition.objects.all()
    context = {
        'competitions': comp_list,
    }

    return render(request, 'competitions.html', context=context)
