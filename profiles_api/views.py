from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models, permissions


class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'gives you the most control over our application logic',
            'is mapped manually to urls'
        ]
        
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        
    def post(self, request):
        """create a message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
            
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def put(self, request, pk=None):
        """handle updating an object"""
        
        return Response({'method': 'PUT'})
        
    def patch(self, request, pk=None):
        """handle partial update of an object"""
        
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        """delete an object"""
        
        return Response({'method': 'DELETE'})
        
class HelloViewSet(viewsets.ViewSet):
    """Test appi viewset"""
    
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return a hello msg"""
        a_viewset = [
            'Uses actions(list, create, retreive....',
            'automatically maps to urls using routers',
            'more functionality with less code'
        ]
        
        return Response({'message':'Hello', 'a_viewset': a_viewset})
        
    def create(self, request):
        """create a new hello msg"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}!'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """handle getting an object by its id"""
        
        return Response({'http_method': 'GET'})
        
    def update(self, request, pk=None):
        return Response({'heep_method': 'PUT'})
        
    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    
    
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
        
class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profles"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
    
    
class UserLoginAPIView(ObtainAuthToken):
    """handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
     