from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DummyData
from .serializers import DummyDataSerializer

class DummyDataList(APIView):
    def get(self, request):
        data = DummyData.objects.all()
        serializer = DummyDataSerializer(data, many=True)
        return Response(serializer.data)