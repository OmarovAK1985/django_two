from django.shortcuts import render
from . import csv_reader
from django.core.paginator import Paginator


def pagin(request):
    page_number = int(request.GET.get('page', 1))
    pag = Paginator(csv_reader.read_csv(), 10)
    page = pag.get_page(page_number)
    values = {
        'list': page,
        'title': 'Страница пагинации',

    }
    return render(request, 'pagination/index.html', values)
