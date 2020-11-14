from django.urls import path
from .views import MMCModelView

urlpatterns = [
    path('mmc', MMCModelView, name='mmc'),
]
