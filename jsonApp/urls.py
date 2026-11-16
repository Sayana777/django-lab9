from django.urls import path
from .views import StudentGetCreate, StudentUpdateDelete, TenhimGetCreate

urlpatterns = [
    path('student/', StudentGetCreate.as_view()),
    path('student/<int:pk>', StudentUpdateDelete.as_view()),
    path('tenhim/', TenhimGetCreate.as_view()),
]