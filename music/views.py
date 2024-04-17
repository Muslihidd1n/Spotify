from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class QoshiqchilarAPI(APIView):
    def get(self, request):
        qoshiqchilar= Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response({"succes":True,"natija": serializer.data })

    def post(self, request):
        qoshiqchi = request.data
        serializer = QoshiqchioPostSerializer(data=qoshiqchi)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":True, "natija": serializer.data})
        return Response(serializer.errors)


class QoshiqchiAPI(APIView):
    def get(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data)

    def put(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.filter(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":True,"updated_data": serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        qoshiqchi.delete()
        return Response({"succes": True, "message":"data deleted"})



class QoshiqlarAPI(APIView):
    def get(self, request):
        qoshiq = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response({"succes":True,"result":serializer.data})


class AlbomlarAPI(APIView):
    def get(self, request):
        albom = Albom.objects.all()
        serializer = AlbomSerializer(albom, many=True)
        return Response({"succes": True, "result": serializer.data})




