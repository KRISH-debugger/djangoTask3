from django.conf.urls import url
from TaskApp1 import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'$',views.home,name='home'),
    url(r'^product$',views.productApi),
    url(r'^hscode$',views.hscodeapi),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
