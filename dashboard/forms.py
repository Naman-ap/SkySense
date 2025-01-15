from django import  forms
from dashboard.models import City
class CityForm(forms.ModelForm):
    class Meta:
        model=City

        fields={'city_name',}
        widgets={
            'city_name':forms.TextInput(attrs={'class':'form-control my-3 justify-content-center','placeholder':'Add your city','style':'width: 20pc;margin-left: 1.5pc;'})
        }

