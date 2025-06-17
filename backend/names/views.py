from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class NameView(APIView):
    def post(self, request):
        name = request.data.get("value")
        if not name:
            return Response({"error": "İsim boş olamaz"}, status=status.HTTP_400_BAD_REQUEST)
        
        person = Person.objects.create(name=name)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)