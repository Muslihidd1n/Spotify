from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *

class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'


    def validate_fayl(self, qiymat):
        if not str(qiymat).endswith('.mp3'):
            raise serializers.ValidationError("Loyiha faqat mp3 fayllar bilan ishalshi mumkin")
        return qiymat


    def validate_davomiylik(self, qiymat):
        if str(qiymat) > "00:06:00":
            raise serializers.ValidationError("Musiqa 6 daqiqadan katta bolmasligi kerak")
        return qiymat


class QoshiqchiSerializer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'


class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class AlbomPostSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'



class QoshiqchioPostSerializer(ModelSerializer):
    class Meta:
        model= Qoshiqchi
        fields = '__all__'

