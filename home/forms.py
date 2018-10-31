from django import forms
from django.contrib.auth.models import User
from .models import *

class login_form (forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}))
	password= forms.CharField(widget=forms.PasswordInput(render_value=False))
#formulario de la tabla material
class agregar_material_form(forms.ModelForm):
	tipo_elemento = forms.ChoiceField(choices=([('Devolutivo','Devolutivo'), ('Consumible','Consumible') ]), initial='1', required = True,)
	class Meta:
		model = Material
		fields = '__all__'
#fromulario de la tabla material
class agregar_marca_form(forms.ModelForm):
	class Meta:
		model = Marca
		fields = '__all__'
		widgets = {
		'nombre' : forms.TextInput(attrs={
			'id' : 'nombre','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
			}),
		}
#formularios de la tabla prestamo
class agregar_prestamoF(forms.ModelForm):
	estado=forms.ChoiceField(choices=([('Activo','Activo'),('Terminado','Terminado')]))
	"""def clean(self):
					
					if any(self.errors):
						return
			
					anchors = []
					urls = []
					duplicates = False
			
					for form in self.forms:
						if form.cleaned_data:
							anchor = form.cleaned_data['anchor']
							url = form.cleaned_data['url']
			
							# Check that no two links have the same anchor or URL
							if anchor and url:
								if anchor in anchors:
									duplicates = True
								anchors.append(anchor)
			
								if url in urls:
									duplicates = True
								urls.append(url)
			
								if duplicates:
									raise forms.ValidationError(
									'Links must have unique anchors and URLs.',
									code='duplicate_links'
								)
			
							# Check that all links have both an anchor and URL
							if url and not anchor:
								raise forms.ValidationError(
									'All links must have an anchor.',
									code='missing_anchor'
								)
							elif anchor and not url:
								raise forms.ValidationError(
									'All links must have a URL.',
									code='missing_URL'
			                    )"""
	class Meta:
		model=Prestamo
		fields='__all__'
		widgets = {
		'fecha_prestamo':forms.TextInput(attrs={
			'type':'date'
			}),
		'fecha_entrega' : forms.TextInput(attrs={
			'type' : 'date'
			})
		}


class agregar_DPrestamoF(forms.ModelForm):
	estado_devolucion=forms.ChoiceField(choices=([('bueno','bueno'),('malo','malo')]))
	class Meta:
		model=Detalle_Prestamo
		fields=['material','estado_devolucion','cantidad']

#-----------------------------------------------------------------------------------------------------

class dev_prestamoF(forms.ModelForm):
	fecha_prestamo=forms.DateField(disabled=True)
	estado=forms.ChoiceField(choices=([('Activo','Activo'),('Terminado','Terminado')]),disabled=True)
	aprendiz=forms.ModelChoiceField(Aprendiz.objects.all(),disabled=True)
	fecha_entrega=forms.DateField(disabled=True)

	class Meta:
		model=Prestamo
		fields='__all__'

class dev_DPrestamoF(forms.ModelForm):
	material=forms.ModelChoiceField(Material.objects.all(),disabled=True)
	estado_devolucion=forms.ChoiceField(choices=([('bueno','bueno'),('malo','malo')]),disabled=True)
	cantidad=forms.IntegerField(disabled=True)
	estado_elemento_prestamo=forms.ChoiceField(choices=([('En Prestamo','En Prestamo'),('Entregado','Entregado')]))
	tipo_daño=forms.ChoiceField(choices=([('Fisico','Fisico'),('Logico','Logico')]))
	fecha_devolucion=forms.DateField()


	class Meta:
		model=Detalle_Prestamo

		fields='__all__'
		widget={
		'cantidad':forms.TextInput(attrs={
		'id':'contador'
		})
		}

#formulario de la tabla categoria
class categoria_form(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = '__all__'
		widgets = {
		'nombre' : forms.TextInput(attrs={
			'id':'nombre','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
			}),
		}

#formulario de la tabla bodega
class agregar_bodega_form(forms.ModelForm):
	class Meta:
		model= Bodega
		fields= '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={
				'id' : 'nombre','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
				}),
		}

#formulario de la tabla cuentadante
class cuentadante_form(forms.ModelForm):
	class Meta:
		model = Cuentadante
		fields = '__all__' 
		widgets = {
		'nombre' : forms.TextInput(attrs={
			'id':'nombre','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
			}),
		'identificacion' : forms.TextInput(attrs={
			'id' : 'identificacion','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus','type':'number'
			}),
		}

#formulario de la tabla programa
class agregar_programas_form(forms.ModelForm):
	class Meta:
		model = Programa
		fields ='__all__'
		widgets = {
			'nombre' : forms.TextInput(attrs={
				'id' : 'nombre','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
				}),
		}

class ficha_form(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'
		widgets= {
			'numero_ficha' : forms.TextInput(attrs={
				'id' : 'ficha','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus','type':'number'
				}),
			'fecha_inicio' : forms.TextInput(attrs={
				'id':'fecha_inicio','class' : 'datepicker','type' : 'date','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
				}),
			'fecha_finalizacion' : forms.TextInput(attrs={
				'id':'fecha_finalizacion','class' : 'datepicker','type' : 'date','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
				}),
		}


#formulario de la tabla bodega_material
class Bodega_Material_form(forms.ModelForm):
	class Meta:
		model = Bodega_Material
		fields = ['bodega','fecha_ingresa','fecha_salida']
		#exclude = ['material']
		widgets= {
			'fecha_ingresa' : forms.TextInput(attrs={
				'class' : 'datepicker','type' : 'date'
				}),
			'fecha_salida' : forms.TextInput(attrs={
				'class' : 'datepicker','type' : 'date'
				}),

		}

class agregar_aprendiz_form(forms.ModelForm):
	class Meta:
		model = Aprendiz
		fields = '__all__'
		widgets = {
			'nombre' : forms.TextInput(attrs={
			'id': 'nombre','class':'form-control','placeholder':'Nombre',
										'autofocus': 'autofocus'
				}),
			'identificacion' : forms.TextInput(attrs={
				'id' : 'identificacion','class':'form-control','placeholder':'Numero de identificacion',
										'autofocus': 'autofocus','type' : 'number'
				}),
			'tipo_documento' : forms.TextInput(attrs={
				'id' : 'tipo_documento','class':'form-control','placeholder':'Numero de identificacion',
										'autofocus': 'autofocus'
				}),
		}