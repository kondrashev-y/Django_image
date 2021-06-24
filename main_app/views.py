from django.shortcuts import render, redirect
from main_app.forms import ImageForm, ResizeImageForm
from main_app.models import Image
from main_app.utils import resize_image


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect(img_obj.get_absolute_url())
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def list_image_view(request):
    image_list = Image.objects.all()
    return render(request, 'main.html', {'image_list': image_list})


def detail_image_view(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResizeImageForm(request.POST)
        if form.is_valid():
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            resize_image(instance=image, width=width, height=height)
    else:
        form = ResizeImageForm()
    return render(request, 'detail.html', {'image': image, 'form': form})
