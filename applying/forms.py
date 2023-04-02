import re
from django import forms
from .models import (
    Academic, Application, ApplicationLanguage, ProfessionalExperience
)
from portal.models import PracticeArea, SpecializationSector


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label="Nome", max_length=200)
    email = forms.CharField(label="E-mail", max_length=50)
    phone = forms.CharField(label="Telefone", max_length=19, required=False)
    address = forms.CharField(label="Address")
    role = forms.CharField(label="Cargo Pretendido",  max_length=20,
                           required=False)
    intend_area = forms.CharField(label="Área Pretendida", max_length=150,
                                  required=False)
    local = forms.CharField(label="Localidade", max_length=20, required=False)
    specialization_sectors = forms.ModelChoiceField(
        queryset=SpecializationSector.objects.all(), required=False
    )
    practice_areas = forms.ModelChoiceField(
        queryset=PracticeArea.objects.all(), required=False
    )
    extra_qualification = forms.CharField(
        label="Qualificações e atividades complementares",
        required=False, widget=forms.Textarea
    )

    class Meta:
        model = Application
        fields = ('name', 'email', 'phone', 'address', 'extra_qualification',
                  'role', 'intend_area', 'local', 'specialization_sectors',
                  'practice_areas')

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role == 'None':
            role = None
        elif role not in ['LAWYER', 'INTERN', 'SUPPORT']:
            role = ''
        return role

    def clean_practice_areas(self):
        practice_areas = self.cleaned_data.get('practice_areas')
        role = self.cleaned_data.get('role')

        if role in ['LAWYER', 'INTERN']:
            if not practice_areas:
                raise forms.ValidationError(
                    'Escolha uma área de atuação válida'
                )
        return practice_areas


class ProfessionalExperienceForm(forms.ModelForm):
    enterprise = forms.CharField(label="Empresa", max_length=50)
    function = forms.CharField(label="Cargo", max_length=50)
    actual_function = forms.BooleanField(label="Cargo Atual", required=False)
    area = forms.CharField(label="Area", max_length=50)
    date_begin = forms.DateField(
        label="Data de Inicio", required=True, input_formats=('%m/%Y',)
    )
    date_finish = forms.DateField(
        label="Data de Término", required=False, input_formats=('%m/%Y',)
    )
    activities = forms.CharField(
        label="Principais atividades desenvolvidas", widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = ProfessionalExperience
        fields = ('enterprise', 'function', 'actual_function', 'area',
                  'date_begin', 'date_finish', 'activities')


class AcademicForm(forms.ModelForm):
    course = forms.CharField(label="Curso", max_length=50)
    institution = forms.CharField(label="Instituição", max_length=100)
    conclusion = forms.IntegerField(label="Ano de conclusão", max_value=9999)
    in_progress = forms.BooleanField(label="Em Progresso", required=False)
    incomplete_course = forms.BooleanField(label="Incompleto", required=False)
    period = forms.CharField(label="Periodo atual", required=False,
                             initial='X')
    shift = forms.CharField(label="Turno do curso", required=False,
                            initial='X')

    class Meta:
        model = Academic
        fields = ('course', 'institution', 'conclusion', 'period', 'shift',
                  'in_progress', 'incomplete_course')

    def clean_conclusion(self):
        year = str(self.cleaned_data['conclusion'])
        r = re.compile('^[1-9][0-9]{3}$')
        if not r.match(year):
            raise forms.ValidationError('Digite um ano válido')
        return int(year)


class ApplicationLanguageForm(forms.ModelForm):
    language = forms.CharField(label="Idioma", max_length=30, required=False)
    level = forms.CharField(label="Nível", max_length=30, required=False)

    class Meta:
        model = ApplicationLanguage
        fields = ('language', 'level')
