from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    # path('login/',views.user_login,name='login'),
    url(r'^user',views.UserModelApi.as_view()),
    url(r'^rentoutahome',views.RentOutAHomeApi.as_view()),
    url(r'^reservedhomes',views.ReservedHomes.as_view()),
    path('',views.dashboard,name='dashboard'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
    path('register/',views.register,name='register')
    , path('rent_out_a_home',views.rent_out_a_home,name='rent_out_a_home'),
    path('rent_a_home',views.rent_a_home,name='rent_a_home'),




]
