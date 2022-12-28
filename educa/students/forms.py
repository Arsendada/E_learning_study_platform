from django import forms
from courses.modules import Course


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
                   queryset=Course.objects.all(),
                   widget=forms.HiddenInput)