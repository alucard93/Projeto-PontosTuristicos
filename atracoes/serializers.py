from rest_framework import serializers
from .models import Atracao


class AtracaoSerializer(serializers.Serializer):
    class Meta:
        model: Atracao
        fields = [
            "id",
            "nome",
            "descricao",
            "horario_func",
            "idade_minima",
        ]
