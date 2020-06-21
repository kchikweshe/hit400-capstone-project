from django.shortcuts import render

# Create your views here.
import os

import pandas
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import View

from .forms import UploadFileForm, DownloadFileForm, UserRegisterForm, CriteriaForm
from .models import *
from .utils.country_decision_maker import decide
from .utils.data_preprocessor import *


def home(request):
    form = UploadFileForm()
    return render(request, 'dashboard/home.html', {'form': form})


def index(request):
    form = DownloadFileForm()
    return render(request, 'dashboard/home.html', {'form': form})


@login_required
def upload(request):
    global countries, alternatives, criteria

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, message="You have successfully uploaded your dataset.")
            csv_file = request.FILES['file']
            countries, alternatives, criteria = load_data(csv_file=csv_file)

            criteria_form = CriteriaForm

            return render(request, 'dashboard/home.html',
                          {'countries': countries, 'criteria': criteria, 'alternatives': alternatives,
                           'criteria_form': criteria_form}, )
        else:
            messages.error(request, message=form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'dashboard/home.html', {
        'form': form
    })


class TemplateFile(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')

        BASE = os.path.dirname(os.path.dirname(os.path.abspath('template.csv')))
        file_path = os.path.join(BASE, 'media/') + 'template.csv'
        if os.path.exists(file_path):
            cd = 'attachment; filename="{0}"'.format(os.path.basename(file_path))
            print("cd = ", cd)

            response['Content-Disposition'] = cd
            # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            print("response = ", response.status_code)
            return response
        return "file not found"


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def rank_countries(request):
    return None


def add_weights(request):
    if request.method == 'POST':

        form = CriteriaForm(request.POST)
        if form.is_valid():
            weights = [form.cleaned_data["w1"], form.cleaned_data["w2"], form.cleaned_data["w3"],
                       form.cleaned_data["w4"],
                       form.cleaned_data["w5"], form.cleaned_data["w6"], form.cleaned_data["w7"]]

            print(weights)

        else:
            print(form.errors)
        # global countries,alternatives,criteria
        #
        # countries,alternatives,criteria=load_data(csv_file=csv)
