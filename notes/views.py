from django.shortcuts import render
from django.http import HttpResponse
from .models import Note


def notes_list_view(request):
    notes = Note.objects.all()
    context = {'notes_list': notes}
    return render(request, 'notes/notes_list.html', context=context)


