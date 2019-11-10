from django import forms  
from employee.models import Employee  
class EmployeeForm(forms.ModelForm):
    ename = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'Angel Fernando'}
    )) 
    eemail = forms.EmailField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'angel_perezh3@outlook.es'}
    ))
    econtact = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'5613141578'}
    ))
    apellido_paterno = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'Pérez'}
    ))
    apellido_materno = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'Hernández'}
    ))
    calle = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'Charles de Gaulle'}
    ))
    colonia = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'La Universal'}
    ))
    municipio = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'Naucalpan'}
    ))
    numeroE = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'12'}
    ))
    numeroI = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'3'}
    ))
    cp= forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'53425'}
    ))
    periodicidad = forms.CharField(widget=forms.TimeInput(
        attrs={'class':'form-control','placeholder':'periodo en dias'}
    ))  
  
    class Meta:  
        model = Employee  
        fields = "__all__"
