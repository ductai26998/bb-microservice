"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


from .views import LoginWithEmailOrUsername, VerifyOTP
from .views import salon as salon_views
from .views import user as user_views
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from service import views as service_views

from .views import salon as salon_views
from .views import user as user_views


router = DefaultRouter()

router.register("users", user_views.UserViewSet)
router.register("salons", salon_views.SalonViewSet)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # url("", include("account.urls")),
    # url("", include("service.urls")),
    # url("", include("booking.urls")),
    url("verifyOTP/", VerifyOTP.as_view(), name="verify_user"),
    url("login/", LoginWithEmailOrUsername.as_view(), name="login"),
    # apis for salon
    url("registerSalon/", salon_views.SalonRegister.as_view(), name="register_salon"),
    # apis for user
    url("registerUser/", user_views.UserRegister.as_view(), name="register_user"),

    path("salonAddress/", salon_views.AddressUpdate.as_view()),
    path("salonBookings/", salon_views.SalonViewSet.as_view({"get": "bookings"})),
    path("userBookings/", user_views.UserViewSet.as_view({"get": "bookings"})),
    path("", include(router.urls)),
]

# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from service import views as service_views

# from .views import salon as salon_views
# from .views import user as user_views

# router = DefaultRouter()

# router.register("users", user_views.UserViewSet)
# router.register("salons", salon_views.SalonViewSet)

# router.register("salonServices", service_views.ServiceSalonViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
#     # apis for salon
#     path("salonAddress/", salon_views.AddressUpdate.as_view()),
#     path("salonBookings/", salon_views.SalonViewSet.as_view({"get": "bookings"})),
#     path("userBookings/", user_views.UserViewSet.as_view({"get": "bookings"})),
#     # apis for user
# ]



# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# # from service import views as service_views

# from .views import salon as salon_views
# from .views import user as user_views

# router = DefaultRouter()

# router.register("users", user_views.UserViewSet)
# router.register("salons", salon_views.SalonViewSet)

# # router.register("salonServices", service_views.ServiceSalonViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
#     # apis for salon
#     # path("salonAddress/", salon_views.AddressUpdate.as_view()),
#     # path("salonBookings/", salon_views.SalonViewSet.as_view({"get": "bookings"})),
#     # path("userBookings/", user_views.UserViewSet.as_view({"get": "bookings"})),
#     # apis for user
# ]
