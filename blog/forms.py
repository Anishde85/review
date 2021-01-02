from django import forms
class GeeksForm(forms.Form):
    title = forms.CharField()
    description=forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))