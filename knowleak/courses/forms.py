from django import forms
  
class FileForm(forms.Form):
    image = forms.ImageField(required=True)

    class Meta:
        fields = ['image']