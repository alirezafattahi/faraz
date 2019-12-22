from django import forms

from .models import person , msg


class proform(forms.ModelForm):

    class Meta:
        model = person 
        fields = ('user' , 'first_name' , 'last_name' , 'father_name' , 'birth_day' , 'employ_date' , 'expire_date' , 'mobile_num' , 'phone_num' , 'address' )

class msgform(forms.ModelForm):

    class Meta:
        model = msg
        fields = ('subject' , 'text' ,)