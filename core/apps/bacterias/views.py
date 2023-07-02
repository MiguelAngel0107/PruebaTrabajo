from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

#
from .models import ConfigVariable
from apps.bacterias.entity.bateria import Bacteria

# Serializers
from .serializers import ConfigVariableSerializer


class CalculateNumberEndBaterias(APIView):

    def post(self, request):
        try:
            bacterias = Bacteria('default', [2, 3, 3, 1, 2])

            for i in range(10):
                print("Serie", i, "---------------------------------------------")
                bacterias.add_bacterias()
                print("---------------------------------------------")

        except Exception as e:
            # Capturar cualquier excepción y devolver un mensaje de error en la respuesta
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({}, status=status.HTTP_200_OK)


class ConfigVariableView(APIView):
    def post(self, request):
        try:
            name_config = request.data['name_config']
            days_maduration = request.data['days_maduration']
            days_reproduction = request.data['days_reproduction']
            number_divisions = request.data['number_divisions']
        except:
            return Response({"error": ""}, status=status.HTTP_400_BAD_REQUEST)

        try:
            config_variable = ConfigVariable.objects.create(name_config=name_config,
                                                            days_maduration=days_maduration,
                                                            days_reproduction=days_reproduction,
                                                            number_divisions=number_divisions)
            serializers = ConfigVariableSerializer(config_variable)
            # Devolver una respuesta de éxito
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Devolver una respuesta de error si ocurre alguna excepción
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
