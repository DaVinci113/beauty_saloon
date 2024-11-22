from django.urls import path, include

from users.views import LoginUser, LogoutUser

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', LogoutUser.as_view(), name='logout'),
]