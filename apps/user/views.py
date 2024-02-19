from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.permissions import AnonPermission
from apps.user.serializers import MyTokenSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenSerializer


