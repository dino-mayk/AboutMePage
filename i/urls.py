from django.urls import path
from i.views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(template_name='i/index.html'), name='home'),
]