from rest_framework import serializers
from IOT.models import Lamp,Usuario,Hist

class LampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lamp
        fields = ['id_lamp','nome','pino']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nome','ra','senha','situacao','admin_acess']

class HistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hist
        fields = ['id_hist','logindate','id_usuario']


