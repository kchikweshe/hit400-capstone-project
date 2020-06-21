from django.conf.urls.static import static

from . import views
from django.urls import path
from django.conf import settings

app_name = 'dashboard'

urlpatterns = [
                  path('', views.upload, name='dashboard-home'),
                    path('add-weights',views.add_weights),
                  path('decide', views.rank_countries, name='home'),
                  # path('', views.upload, name="csv_upload")
                  # url('template_file/', views.download, name='csv_download'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)