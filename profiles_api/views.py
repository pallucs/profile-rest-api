from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from profiles_api import serializers


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