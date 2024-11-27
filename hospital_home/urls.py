from django.contrib import admin
from django.urls import path, include, re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),
    path('accounts/login/', views.signupsignin, name="login_required"),
    path('signupsignin/signin', views.signin, name='signin'),
    path('signupsignin/signup', views.signup, name='signup'),
    path('predict/', views.predictview, name="predictview"),
    path('signupsignin/', views.signupsignin, name='signupsignin'),
    path('services/schedule/', views.schedule, name='Schedule'),
    path('schedule/', views.schedule, name="schedule"),
    path('schedule/schedule_apt', views.schedule_apt, name="scheduleapt"),
    path('fordoctors/', views.fordoctors, name="fordoctors"),
    path('fordoctors/schedule', views.fordoctorsnext, name="fordoctors"),
    # path('schedule/predict', views.predict, name="predict"),
    path('services/', views.services, name="services"),
    path('book/<str:doctor>/<str:patient>/', views.book, name='book'),
    path('contact/', views.contactus, name="contactus"),
    path('contact/submit', views.submit, name="contactussubmit"),
]
