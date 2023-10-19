from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, redirect

from .models import *
from django.http import HttpResponse
import requests
import json
from django.http.response import JsonResponse
from .forms import *

def index(request):
    context = {}
    return render(request, "index.html", context)


@staff_member_required
def create_img_type(request):
    if request.method == 'POST':
        img_type_name = request.POST.get('img_type_name')
        new_image_value = request.POST.get('new_image', '1')

        if img_type_name:
            # Use the correct field name "ImgTypes" in the ImageType model
            img_type, created = ImageType.objects.get_or_create(ImgTypes=img_type_name, new_img=new_image_value)

            if created:
                message = "Category created successfully."
            else:
                message = "Category already exists."

            return render(request, 'add.html', {'message': message})

    return render(request, 'add.html')


@staff_member_required
def aaa(request):
    uploaded_image_url = None

    if request.method == 'POST':
        form = ImgsForm(request.POST, request.FILES)
        if form.is_valid():
            img_instance = form.save()
            uploaded_image_url = request.build_absolute_uri(img_instance.pic.url)
            img_instance.image_url = uploaded_image_url
            img_instance.save()
    else:
        form = ImgsForm()

    return render(request, 'img.html', {'form': form, 'uploaded_image_url': uploaded_image_url})


@staff_member_required
def add_img_withTypeType(request):
    uploaded_image_urls = []

    if request.method == 'POST':
        form = ImgsForm(request.POST, request.FILES)
        if form.is_valid():
           
            images = request.FILES.getlist('pic')

            for image_file in images:
                
                img_instance = Imgs(pic=image_file)
                
                img_instance.ID_Type = form.cleaned_data['ID_Type']
                
                img_instance.save()

                uploaded_image_url = request.build_absolute_uri(img_instance.pic.url)
                
                img_instance.image_url = uploaded_image_url
                img_instance.save()

                uploaded_image_urls.append(uploaded_image_url)

    else:
        form = ImgsForm()

    return render(request, 'img.html', {'form': form, 'uploaded_image_urls': uploaded_image_urls})

def imgtypes_api(request):
    data = ImageType.objects.all().order_by('-id')
    response = {

        'ImgsTypesModel': list(data.values('id','ImgTypes','new_img'))
        #'guests': dict(data.values('name','mobile'))

    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})



def imgsapi (request,id):
    imgtype = ImageType.objects.get(id=id)
    img=Imgs.objects.all().order_by('-id').filter(ID_Type_id=imgtype.id)

    response = {
        'ImgsModel':list(img.values('id','ID_Type_id','new_img','image_url'))

    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})