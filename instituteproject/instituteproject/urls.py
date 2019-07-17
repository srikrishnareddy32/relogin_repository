
from django.contrib import admin
from django.conf.urls import url
from instituteapp import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.base),
    url(r'^home/',views.home),
    url(r'^contact/',views.contacts),
    url(r'^courses/',views.course),
    url(r'^feedback/',views.feedback),
    url(r'^team/',views.team),
    url(r'^gallery/',views.gallery),
]
