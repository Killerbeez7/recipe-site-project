from django.urls import path
from recipe_site.common.views import IndexView, about, contacts

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
