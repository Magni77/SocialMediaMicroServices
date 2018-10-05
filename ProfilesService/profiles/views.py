from rest_framework.generics import RetrieveUpdateAPIView

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        return Profile.objects.all()
