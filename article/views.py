from django.shortcuts import render

# Create your views here.
from .forms import SubscriberForm


def article(request):
    name = "ПрофиСПб"
    current_day = "00,00,0000"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/test.html', locals())
