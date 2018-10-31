from rest_framework import serializers
from home.models import *


class Cuentadante_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cuentadante
		fields = ('url','nombre','identificacion',)


class prestamo_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Prestamo
		fields = ('url','fecha_prestamo','estado','aprendiz','fecha_entrega',)

class Aprendiz_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Aprendiz
		fields = ('url','nombre','identificacion','tipo_documento','estado','ficha',)

class Ficha_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ficha
		fields = ('url','numero_ficha','fecha_inicio','fecha_finalizacion','listado','programa',)

class Programa_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Programa
		fields = ('url','nombre')
class Detalle_Prestamo_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Detalle_Prestamo
		fields = ('url','material','prestamo','estado_devolucion','cantidad','estado_elemento_prestamo','descripcion','tipo_daño','fecha_devolucion')

class Material_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Material		
		fields = ('url','tipo_elemento','nombre','codigo_sena','cantidad','estado','marca','categoria','cuentadante','ficha','imagen')