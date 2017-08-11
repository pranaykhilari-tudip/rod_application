from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from rodapp import views
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r"^accounts/signup/$", views.UserSignup.as_view(), name="account_signup"),
    url(r"^accounts/login/$", views.UserLogin.as_view(), name="account_login"),
    url(r"^$",views.is_user_authenticated),
    url(r"^logout/$",views.user_logout),
    url(r'^accounts/', include('allauth.urls')),
]
