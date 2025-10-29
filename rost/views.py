from django.shortcuts import render, redirect


def home(request):

    context = {
        'title': 'Домашняя страница',
    }

    return render(request, 'rost/home.html', context)


def login_user(request):

    context = {
        'title': 'Авторизация',
    }

    return render(request, 'rost/login.html', context)
