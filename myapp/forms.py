from django import forms
from .models import Svcs, Indl, Country, GovtOrder, Course, CourseOffer, CourseAcceptance, Visit, YearlyState

class SvcsForm(forms.ModelForm):
    class Meta:
        model = Svcs
        fields = '__all__'

class IndlForm(forms.ModelForm):
    class Meta:
        model = Indl
        fields = '__all__'

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class GovtOrderForm(forms.ModelForm):
    class Meta:
        model = GovtOrder
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CourseOfferForm(forms.ModelForm):
    class Meta:
        model = CourseOffer
        fields = '__all__'

class CourseAcceptanceForm(forms.ModelForm):
    class Meta:
        model = CourseAcceptance
        fields = '__all__'

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

class YearlyStateForm(forms.ModelForm):
    class Meta:
        model = YearlyState
        fields = '__all__'

