from django.shortcuts import render
from home.models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.





class cuentadante_viewset(viewsets.ModelViewSet):
	queryset = Cuentadante.objects.all()
	serializer_class = Cuentadante_serializer

class prestamo_viewset(viewsets.ModelViewSet):
	queryset = Prestamo.objects.all()
	serializer_class = prestamo_serializer

class Aprendiz_viewset(viewsets.ModelViewSet):
	queryset = Aprendiz.objects.all()
	serializer_class = Aprendiz_serializer

class ficha_viewset(viewsets.ModelViewSet):
	queryset = Ficha.objects.all()
	serializer_class = Ficha_serializer

class programa_viewset(viewsets.ModelViewSet):
	queryset = Programa.objects.all()
	serializer_class = Programa_serializer

class Detalle_Prestamo_viewset(viewsets.ModelViewSet):
	queryset = Detalle_Prestamo.objects.all()
	serializer_class = Detalle_Prestamo_serializer

class Material_viewset(viewsets.ModelViewSet):
	queryset = Material.objects.all()
	serializer_class = Material_serializer