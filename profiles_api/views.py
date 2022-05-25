from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'gives you the most control over our application logic',
            'is mapped manually to urls'
        ]
        
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        