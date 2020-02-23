from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import ItemForm
from .models import Item


def index(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            Item(
                name=form.cleaned_data['name'],
                owner=request.user,
                time_entered=form.cleaned_data['time_entered'],
                expiration_date=form.cleaned_data['expiration_date']
            ).save()
            return HttpResponseRedirect('/')

    else:
        form = ItemForm()

    items = Item.objects.all()
    user_count = User.objects.all().count()
    return render(request, 'index.html', {"items": items, "form": form, "user_count": user_count})
