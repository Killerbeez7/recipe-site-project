from django.urls import path
from recipe_site.profiles.views import profile_details
import recipe_site.profiles.signals

urlpatterns = (
    path('', profile_details, name='profile details'),
)




