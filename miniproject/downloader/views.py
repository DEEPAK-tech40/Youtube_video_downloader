from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from . import forms
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import youtube_dl
from . import models
from django.contrib.auth.models import User
# Create your views here.

class Index(TemplateView):
    template_name = 'downloader/YT_Downloader(Home).html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'downloader/signup.html'

#class Down(TemplateView,LoginRequiredMixin):
#    login_url = '/login/'
#    template_name = 'downloader/YT_Downloader(downloader).html'


def Downloader(request):

    if request.method == 'POST':
        video_url = request.POST['link']
        history = models.User_downloads(user=User.objects.get(username=request.user.username),Video_downloaded=video_url)
        history.save()
#        return HttpResponse("Success")
        #return HttpResponse("<script src='{src}'></script>".format(src = staticfiles.static('static/js/YT_Downloader(downloader).js')))
        if video_url:
            ydl_out = {'outtmp': 'D:/'}
            messages.success(request,'Downloading')
            with youtube_dl.YoutubeDL(ydl_out) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Dowmloaded. ')
            return render(request,'downloader/YT_Downloader(downloader).html')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return render(request,'downloader/YT_Downloader(downloader).html')
    return render(request,'downloader/YT_Downloader(downloader).html')
