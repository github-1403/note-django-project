from django.shortcuts import render
from django.http import HttpResponse


def notes_list_view(request):
    return HttpResponse('notes list')

