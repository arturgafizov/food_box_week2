from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from users.models import User
from users.models import UserSerializer, UserCurrentSerializer


class UserList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CurrentUserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserCurrentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
