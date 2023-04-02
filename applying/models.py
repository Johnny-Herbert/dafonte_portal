from django.db.models import (
    Model, TextField, CharField, BooleanField, ForeignKey, CASCADE,
    IntegerField, DateTimeField, DateField, SET_NULL
)

from portal.models import Opportunity, PracticeArea, SpecializationSector

from datetime import datetime


class Application(Model):
    ROLE_CHOICES = (
        ('LAWYER', 'Advogado'),
        ('INTERN', 'Estagiário'),
        ('SUPPORT', 'Equipe de apoio'),
    )
    LOCAL_CHOICES = (
        ('RC', 'Recife'),
        ('SL', 'Salvador'),
        ('BS', 'Brasília'),
        ('SP', 'São Paulo'),
    )

    name = CharField("Nome", max_length=200)
    email = CharField("E-mail", max_length=50)
    phone = CharField("Telefone", max_length=19, default="")
    address = TextField("Address")
    role = CharField("Cargo", max_length=20, choices=ROLE_CHOICES, blank=True)
    intend_area = CharField("Área Pretendida", max_length=150, blank=True)
    local = CharField(
        "Localidade", max_length=20, choices=LOCAL_CHOICES, blank=True
    )
    extra_qualification = TextField(
        "Qualificações e atividades complementares", default=""
    )
    opportunity = ForeignKey(
        Opportunity, related_name="related_applications", null=True,
        blank=True, on_delete=SET_NULL
    )

    practice_areas = ForeignKey(
        PracticeArea, related_name="related_applications", null=True,
        blank=True, on_delete=SET_NULL, verbose_name="Área de Atuação"
    )
    specialization_sectors = ForeignKey(
        SpecializationSector, related_name="related_applications", null=True,
        blank=True, on_delete=SET_NULL, verbose_name="Setor de Especialização"
    )

    created_at = DateTimeField("Enviado em", default=datetime.now)

    # atributo para identificar se o admin gerou e realizou o download do pdf
    is_downloaded = BooleanField("Visualizado", default=False)

    class Meta:
        verbose_name = "currículo"
        verbose_name_plural = "currículos"

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    def change_download_ok(self):
        """
        Atualiza o atributo que identifica se o curriculo foi
        visualizado/baixado
        """
        if not self.is_downloaded:
            self.is_downloaded = True
            self.save()


@property
def related_professional(self):
    return self.application.related_professional


class ProfessionalExperience(Model):
    enterprise = CharField("Empresa", max_length=50)
    function = CharField("Cargo", max_length=50)
    actual_function = BooleanField("Cargo Atual", blank=True, default=False)
    area = CharField("Area", max_length=50)
    date_begin = DateField(verbose_name="Data de Inicio", blank=True,
                           null=None)
    date_finish = DateField(verbose_name="Data de término", blank=True,
                            null=True)
    activities = TextField("Principais atividades desenvolvidas")
    application = ForeignKey(Application, CASCADE,
                             related_name="related_professional")

    class Meta:
        verbose_name = "experiência profissional"
        verbose_name_plural = "experiências profissionais"

    def __str__(self):
        return "{} - {}/{}".format(self.enterprise, self.function,
                                   self.application.name)


class Academic(Model):
    PERIOD_CHOICES = (
        ('X', 'Concluído'),
        ('1', '1º Período'),
        ('2', '2º Período'),
        ('3', '3º Período'),
        ('4', '4º Período'),
        ('5', '5º Período'),
        ('6', '6º Período'),
        ('7', '7º Período'),
        ('8', '8º Período'),
        ('9', '9º Período'),
        ('10', '10º Período'),
        ('12', '12º Período'),
    )
    SHIFT_CHOICES = (
        ('X', 'Concluído'),
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    )
    course = CharField("Curso", max_length=50)
    institution = CharField("Instituição", max_length=100)
    conclusion = IntegerField("Ano de conclusão")
    application = ForeignKey(Application, CASCADE,
                             related_name="related_academic")

    incomplete_course = BooleanField("Curso incompleto", blank=True,
                                     default=False)
    in_progress = BooleanField("Em progresso", blank="True", default=False)
    period = CharField("Período", max_length=20, choices=PERIOD_CHOICES,
                       blank=True)
    shift = CharField("Turno", max_length=20, choices=SHIFT_CHOICES,
                      blank=True)

    class Meta:
        verbose_name = "formação acadêmica"
        verbose_name_plural = "formações acadêmicas"

    def __str__(self):
        return "{} - {} /{}".format(self.course, self.institution,
                                    self.application.name)


class ApplicationLanguage(Model):
    LEVEL_CHOICES = (
        ('beginner', 'Básico'),
        ('intermediate', 'Intermediário'),
        ('advanced', 'Avançado')
    )
    language = CharField("Idioma", max_length=30)
    application = ForeignKey(Application, CASCADE,
                             related_name="related_idioms")
    level = CharField("Nível", max_length=30, choices=LEVEL_CHOICES,
                      blank=True, null=True)

    class Meta:
        verbose_name = "idioma"
        verbose_name_plural = "idiomas"
        ordering = ['language']

    def __str__(self):
        return self.language
