from django.shortcuts import render
from . import form

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def recipies_list(request):
    values = {
        'title': 'Список блюд',
        'list': DATA,

    }
    return render(request, 'recipes/index.html', values)


def recipe(request, name):
    count = request.GET.get('count')

    if count is not None:
        count = int(count)
        if count < 1:
            count = 1
    my_dict = dict()
    for k, v in DATA.items():
        if name == k:
            for keys, value in v.items():
                my_dict.setdefault(keys, value)
                if count is not None:
                    a = value * count
                    my_dict.update({keys: a})
            values = {
                'title': 'Рецепт',
                'my_dict': my_dict,
                'name': name,
                'form': form.form_for_number,
                'count': count,
            }
            return render(request, 'recipes/recipe.html', values)
