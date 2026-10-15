from django.shortcuts import render
from .forms import UserForm

def index(request):
    form = UserForm()
    return render(request, 'tasks/index.html', {'form': form})

def postuser(request):
    if request.method == 'POST':
        form =UserForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            return render(request, 'tasks/index.html', {'data': cleaned_data})

    else:
        form = UserForm()

    return render(request, 'tasks/index.html', {'form': form})