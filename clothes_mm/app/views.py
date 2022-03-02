from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from . import image_detection
from . import path
import os


def index(request):
    return render(request, 'home.html')


def search(request):

    try:
        if request.method == 'POST' and request.FILES['upload']:
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            print('Image name', upload.name)
            file = fss.save('temp/' + upload.name, upload)
            file_url = fss.url(file)

            print(file_url)

            path.DETECT_NAME, _ = image_detection.detection(
                os.path.join(path.TEMP_DIR, upload.name))
            #os.remove(os.path.join(path.TEMP_DIR, upload.name))
            print(path.DETECT_NAME)
            return redirect('/clothes')

    except:
        pass

    return render(request, 'search.html')


def show_clothes(request):
    context = {'detect_name': path.DETECT_NAME}

    print(path.DETECT_NAME)

    if path.DETECT_NAME == "amarapura_design":
        images_name = os.listdir(os.path.join(
            path.STATIC_DIR, 'images/amarapura_design'))
        # print(images_name)
        images_path = []
        for image in images_name:
            images_path.append('images/amarapura_design/'+image)

        # print(images_path)
        context = {'detect_name': 'Amarapura Design', 'images': images_path}
        # print(context)
        return render(request, 'clothes.html', context)

    if path.DETECT_NAME == "chate_design":
        images_name = os.listdir(os.path.join(
            path.STATIC_DIR, 'images/chate_design'))
        # print(images_name)
        images_path = []
        for image in images_name:
            images_path.append('images/chate_design/'+image)

        # print(images_path)
        context = {'detect_name': 'Chate Design', 'images': images_path}
        # print(context)
        return render(request, 'clothes.html', context)

    if path.DETECT_NAME == "innlay_design":
        images_name = os.listdir(os.path.join(
            path.STATIC_DIR, 'images/innlay_design'))
        # print(images_name)
        images_path = []
        for image in images_name:
            images_path.append('images/innlay_design/'+image)

        # print(images_path)
        context = {'detect_name': 'Innlay Design', 'images': images_path}
        # print(context)
        return render(request, 'clothes.html', context)

    if path.DETECT_NAME == "sanmyan_design":
        images_name = os.listdir(os.path.join(
            path.STATIC_DIR, 'images/sanmyan_design'))
        # print(images_name)
        images_path = []
        for image in images_name:
            images_path.append('images/sanmyan_design/'+image)

        # print(images_path)
        context = {'detect_name': 'Sanmyan Design', 'images': images_path}
        # print(context)
        return render(request, 'clothes.html', context)

    return render(request, 'clothes.html', context)
