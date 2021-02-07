from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet


from users.models import User
from users.models import UserSerializer, UserCurrentSerializer


class UserList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserCurrentSerializer

    def get_object(self):
        return self.request.user
