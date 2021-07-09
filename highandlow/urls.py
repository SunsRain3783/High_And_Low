from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from HighAndLow import views

index_view = TemplateView.as_view(template_name="registration/index.html")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path('', include("HighAndLow.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
