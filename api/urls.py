from django.urls import path
from .views import MMCModelView, MMCCModelView, MM1KModelView, MM1InfMModelView

urlpatterns = [
    path('mmc', MMCModelView, name='mmc'),
    path('mmcc', MMCCModelView, name='mmcc'),
    path('mm1k', MM1KModelView, name='mm1k'),
    path('mm1infm', MM1InfMModelView, name='mm1infm'),
]
