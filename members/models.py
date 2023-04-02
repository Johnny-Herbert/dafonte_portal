from abc import abstractmethod
from datetime import datetime

from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from dafonte_portal.utils import upload_to


class MemberType(models.Model):
    # Tipos de Membros e seus IDs
    LAWYER = 1
    ADMINISTRATIVE_STAFF = 2
    TRAINEE = 3
    INTERN = 4

    name = models.CharField("Nome", max_length=50)

    class Meta:
        verbose_name = "tipo de membro"
        verbose_name_plural = "tipos de membro"

    def __str__(self):
        return self.name


class JobTitle(models.Model):
    name = models.CharField("Nome", max_length=50)

    class Meta:
        verbose_name = "título da função"
        verbose_name_plural = "titulos das funções"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Member(models.Model):
    first_name = models.CharField("Nome", max_length=50, default="")
    last_name = models.CharField("Sobrenome", max_length=50, default="")
    photo = models.ImageField("Foto", blank=True, null=True, upload_to=upload_to)
    type = models.ForeignKey(MemberType, models.PROTECT, verbose_name="Tipo de Membro", related_name="members")

    class Meta:
        verbose_name = "membro"
        ordering = ["first_name"]

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

class AwardMembers(models.Model):
    picture = models.ImageField("Imagem", blank=True, null=True, upload_to=upload_to)
    publication_date = models.DateField("Data de Publicação", default=datetime.now)
    title = models.CharField("Título", max_length=100, default="")
    description = RichTextUploadingField("Descrição", default="", max_length=100)

    class Meta:
        verbose_name = "prêmios de advogado"

    def __str__(self):
        return self.title

class MemberChild:
    @property
    @abstractmethod
    def member(self):
        pass

    @property
    def first_name(self):
        return self.member.first_name

    @property
    def last_name(self):
        return self.member.last_name

    @property
    def photo(self):
        return self.member.photo

    @property
    def full_name(self):
        return self.member.full_name

    @property
    def related_publications(self):
        return self.member.related_publications

    @property
    def related_events_lawyers(self):
        return self.member.related_events_lawyers


class MemberLawyer(models.Model, MemberChild):
    # type = 1
    email = models.CharField("E-mail", max_length=50)
    phone = models.CharField("Telefone", max_length=19, default="")
    vcard = models.FileField(blank=True, null=True, upload_to=upload_to)
    academic_formation = RichTextUploadingField("Formação Acadêmica")
    professional_experience = RichTextUploadingField("Experiência Profisisonal")
    awards_and_publications = RichTextUploadingField("Prêmios e Publicações", blank=True)
    other_activities = RichTextUploadingField("Outras Atividades", default="", blank=True)
    member = models.OneToOneField(Member, models.CASCADE, related_name="lawyer")
    practice_areas = models.ManyToManyField("portal.PracticeArea", verbose_name="Áreas de Atuação", related_name="lawyers", blank=True)
    specialization_sector = models.ManyToManyField("portal.SpecializationSector", verbose_name="Setor de Especialização", related_name="lawyers", blank=True)
    languages = models.ManyToManyField("portal.Language", verbose_name="Idiomas", related_name="lawyers")
    awards = models.ManyToManyField(AwardMembers, verbose_name="Prêmios", related_name="lawyers", blank=True)

    class Meta:
        verbose_name = "advogado"
        ordering = ["member__first_name"]

    def __str__(self):
        return self.member.full_name


class MemberAdministrativeStaff(models.Model, MemberChild):
    # type = 2
    member = models.OneToOneField(Member, models.CASCADE, related_name="administrative_staff")
    job_title = models.ForeignKey(JobTitle, models.PROTECT, verbose_name="Nome da Função", related_name="members")

    class Meta:
        verbose_name = "membro da equipe administrativa"
        verbose_name_plural = "membros da equipe administrativa"
        ordering = ["member__first_name"]

    def __str__(self):
        return self.member.full_name


class MemberTrainee(models.Model, MemberChild):
    # type = 3
    member = models.OneToOneField(Member, models.CASCADE, related_name="trainee")
    practice_areas = models.ManyToManyField("portal.PracticeArea", verbose_name="Áreas de Atuação", related_name="trainees", blank= True)
    specialization_sectors = models.ManyToManyField("portal.SpecializationSector", related_name="trainees", blank= True)

    class Meta:
        verbose_name = "trainee"
        ordering = ["member__first_name"]

    def __str__(self):
        return self.member.full_name


class MemberIntern(models.Model, MemberChild):
    # type = 4

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    member = models.OneToOneField(Member, models.CASCADE, related_name="intern")
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    practice_areas = models.ManyToManyField("portal.PracticeArea", related_name="interns", blank= True)
    specialization_sectors = models.ManyToManyField("portal.SpecializationSector", related_name="interns", blank= True)

    class Meta:
        verbose_name = "estagiário"
        ordering = ["member__first_name"]

    def __str__(self):
        return self.member.full_name

