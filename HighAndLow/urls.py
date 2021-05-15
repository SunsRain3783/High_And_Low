from django.urls import path

from .views import IndexView, SoloView, MultiView

urlpatterns = [
    path('', IndexView.as_view()),
    path('1p/', SoloView.as_view()),
    path('2p/', MultiView.as_view()),
]
