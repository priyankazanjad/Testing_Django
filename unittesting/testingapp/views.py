from django.shortcuts import render
from .models import Name
from .forms import NameForm


# Create your views here.
def func(request):
    form = NameForm()

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()

    names = Name.objects.all()
    context = {
        "names": names,
        "form": form,
    }

    return render(request, "testingapp/index.html", context)