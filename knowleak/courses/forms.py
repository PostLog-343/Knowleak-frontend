from django import forms
  
class FileForm(forms.Form):
    image = forms.ImageField()

    class Meta:
        fields = ['image']