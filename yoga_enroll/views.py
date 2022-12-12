from django.shortcuts import render, redirect
from django.http import HttpResponse, response
# Create your views here.
from yoga_enroll import models

from .forms import create_yogaRegi_form

def home(request):
    form = create_yogaRegi_form()

    error = 'Errors in the form, please verify.'

    context = {
        
    }

    if request.method == 'POST':
        form = create_yogaRegi_form(request.POST)
        #print(form.cleaned_data['Name'])
        if form.is_valid():
            form.save()
            return redirect('success', form.instance.id)
        else:
            context['error'] = error

    context['form'] = form


    return render(request, 'yoga_enroll/index.html', context)


def success(request, pk):
  obj = models.Student.objects.get(pk=pk)
  context = {
      'name': obj.name
  }
  return render(request, 'yoga_enroll/success.html', context)