from django.urls import  path
from main.models import link_uch

from main import views

app_name = 'main'
i = link_uch.objects.order_by()
urlpatterns = [
    path('', views.glavnaya, name="glavnaya"),
    path('glavnaya', views.glavnaya, name="glavnaya"),
    path('about_me', views.aboutme, name="aboutme"),
    path('algebra', views.algebra, name="algebra"),
    path('geometria', views.geometria, name="geometria"),
    path('oge_ege', views.oge_ege, name="oge_ege"),
    path('interesting', views.interesting, name="interesting"),
    path('library', views.library, name="library"),
    path('olympiads', views.olimpiads, name="olimpiads"),

]
