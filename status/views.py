from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from status.serializers import StatusSerializer
from status.models import Status
# Create your views here.
class StatusView(APIView):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        status=Status.objects.get(pk=id)
        serializer=StatusSerializer(status,many=False)

        return Response(serializer.data)

# using class based view
# class SatausListView(APIView):
#     def get(self,request):
#         all_status=Status.objects.all()
#         serializer=StatusSerializer(all_status,many=True)
#         return Response(serializer.data)

#using generic views
class StatusListView(generics.ListAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

class CreateStatusView(generics.CreateAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

class StatusDetailView(generics.RetrieveAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

class StatusUpdateView(generics.UpdateAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

class StatusDeleteView(generics.DestroyAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer



