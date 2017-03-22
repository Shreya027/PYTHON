from django import forms

 
class StudentForm(forms.Form):
    name = forms.CharField()
    team_name = forms.CharField()
    sap_id = forms.CharField()
    branch = forms.CharField()
    year = forms.CharField()
    







