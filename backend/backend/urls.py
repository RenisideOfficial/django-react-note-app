from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""deals with how incoming web requests are directed to
the python code the (views/routes)"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # call the view we just created and allow us to make a new user
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    # any request with "api/" will get forwarded to the api folder/url.py file
    path("api/", include("api.urls"))
]
