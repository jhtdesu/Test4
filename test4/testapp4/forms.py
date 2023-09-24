from .models import Blog

from django import forms

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Blog
        fields = ['title','author','content']

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Blog
        fields = ['title','author','content']