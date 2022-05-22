from django.urls import path,re_path
from . import views


urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    #path('download/',views.Down.as_view(),name='downloader'),
    path('',views.Index.as_view(),name='home'),
    path('download/',views.Downloader,name='downloader')
]
