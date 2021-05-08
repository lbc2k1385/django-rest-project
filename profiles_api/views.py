from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Returns a list of API view"""
        an_api_view = [
            "uses http methods as functions (get, post, put, patch, delete)",
            "is similar to traditional django view",
            "gives most control over app logic",
            "is mapped manually to urls"
        ]

        return Response({'message': 'Hello', 'an_api_view': an_api_view})

    def post(self, request):
        """Create Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Updating specific attribute"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """Delete object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Actions (list, create, retrieve, update, partial_update'
            'auto maps using routers',
            'provides more functinoality w/ less code '
        ]
        return Response({'message': 'Hello', 'set': a_viewset})

    def create(self, request, pk=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting object by id"""
        return Response({'http_method': 'Get'})

    def update(self, request, pk=None):
        """Handlue updating object"""
        return Response({'http_method:': 'PUT'})

    def partial_update(self, request, pk=None):
        """Update part of object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete object"""
        return Response({'http_method': 'DELETE'})


class UserprofileViewSet(viewsets.ModelViewSet):
    """"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')


