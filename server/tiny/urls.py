from django.conf.urls import url
from .views import TinyView

urlpatterns = [
    url(r'^tiny/(?P<tiny_id>.*)', TinyView.as_view()),
]
