from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'Password updated successfully.'
        }, status=status.HTTP_200_OK)