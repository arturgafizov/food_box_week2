from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserList
from users.views import CurrentUserRetrieveUpdateView


urlpatterns_users = [
    path('auth/register/', UserList.as_view(), name='UserList'),  # local item url created
    path('auth/login/', obtain_auth_token),
    path('current/', CurrentUserRetrieveUpdateView.as_view(), name='CurrentUser'),
]
