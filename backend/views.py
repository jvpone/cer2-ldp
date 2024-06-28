from rest_framework import viewsets, generics
from rest_framework.views import APIView #
from rest_framework.response import Response #
from rest_framework.renderers import JSONRenderer #
from backend.models import Number, Pokemon
from backend.serializers.NumberSerializer import NumberSerializer
from backend.serializers.PokemonSerializer import PokemonSerializer
from backend.renderers import PokemonHTMLRenderer #


import math
import random
import string

class NumberViewSet(viewsets.ModelViewSet):

    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    def get_queryset(self):
        """
        Opcionalmente restringe los números devueltos al valor de 'number' que
        sea igual a 10, pasando un parámetro de consulta `number=10` en la URL.
        """
        queryset = Number.objects.all()
        number = self.request.query_params.get('number', None)
        if number is not None:
            queryset = queryset.filter(number=number)
        return queryset

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    # def get_queryset(self):
    #     """
    #     Opcionalmente restringe los números devueltos al valor de 'number' que
    #     sea igual a 10, pasando un parámetro de consulta `number=10` en la URL.
    #     """
    #     queryset = Number.objects.all()
    #     number = self.request.query_params.get('number', None)
    #     if number is not None:
    #         queryset = queryset.filter(number=number)
    #     return queryset


class CreateRandomNumber(generics.CreateAPIView):
    serializer_class = NumberSerializer

    def perform_create(self, serializer):
        # Generar un número aleatorio entre 1 y 100
        random_number = random.randint(1, 100)
        # Generar una letra aleatoria
        random_letter = random.choice(string.ascii_uppercase)
        # Guardar el número y la letra aleatorios en la base de datos
        serializer.save(number=random_number, letter=random_letter)


# vista para la imagen

class PokemonListView(APIView):
    renderer_classes = [PokemonHTMLRenderer, JSONRenderer]
    template_name = 'pokemon_list.html'

    def get (self,request):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        if request.accepted_renderer.format == 'html':
            return Response({'pokemons': serializer.data})
        return Response(serializer.data)
    

#vista del torneo
