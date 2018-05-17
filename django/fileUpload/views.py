from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to
from django import forms
from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response
import os

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file  = forms.FileField()


@render_to('fileUpload:home.html')
@login_required
def home(request):
    path = "/tmp/uploadDir"
    if not os.path.exists(path):
        os.makedirs(path)
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name
            fp = open('%s/%s' % (path, filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            filelists = os.listdir(path)
            return {
                "message": "Success",
                "filelists": filelists
            }
        else:
            return {
                "message": " fileUpload!",
                "app_name": "fileUpload"
            }
    else:
        filelists = os.listdir(path)
        return {
            "message": "Ready!",
            "app_name": "fileUpload",
            "filelists": filelists
        }
