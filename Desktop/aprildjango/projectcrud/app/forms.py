from django import forms
from app.models import Schoolbranch, ExamModel

class SchoolbranchForm(forms.ModelForm):
    class Meta :
        model = Schoolbranch
        fields = "__all__"   # for all fields of model class/   exclude =  not req fiels


class Examforms(forms.ModelForm):
    class Meta :
        model = ExamModel
        fields = "__all__"