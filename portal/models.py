from datetime import datetime
from itertools import chain

from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db.models import (
    Model, FileField, ImageField, TextField, CharField, BooleanField,
    SlugField, ForeignKey, CASCADE, ManyToManyField, PROTECT,
    IntegerField, DateTimeField, DateField, TimeField, URLField,
    PositiveSmallIntegerField
)

from dafonte_portal.utils import upload_to


class SiteParameter(Model):
    name = SlugField("Nome", max_length=30, unique=True)
    value = TextField("Valor", blank=True, null=True)
    file = FileField("Arquivo", blank=True, upload_to=upload_to, null=True)

    class Meta:
        verbose_name = "parâmetro do site"
        verbose_name_plural = "parâmetros do site"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def clean(self):
        if self.value is None and self.file.name is None:
            raise ValidationError("Valor ou Arquivo devem ser preenchidos")


class Page(Model):
    title = CharField("Título", max_length=200, unique=True)
    slug = SlugField("Slug", unique=True)
    background_image = ImageField(
        "Imagem de Fundo", blank=True, null=True, upload_to=upload_to)

    # parameters = PageParameter

    class Meta:
        verbose_name = "página"
        ordering = ["title"]

    def __str__(self):
        return self.title


class PageParameter(Model):
    name = SlugField("Nome", max_length=30)
    value = TextField("Valor", default='', blank=True)

    page = ForeignKey(Page, CASCADE, verbose_name="Página",
                      related_name="parameters")

    class Meta:
        verbose_name = "parâmetro de página"
        verbose_name_plural = "parâmetros de página"
        ordering = ["name"]
        unique_together = [("page", "name")]

    def __str__(self):
        return self.name

    def clean(self):
        if self.value is None and self.file is None:
            raise ValidationError("Valor ou Arquivo devem ser preenchidos")


class PracticeArea(Model):
    name = CharField("Nome", max_length=100, unique=True)
    description = RichTextField("Descrição", blank=True, null=True)
    picture = ImageField("Imagem", blank=True, null=True, upload_to=upload_to)

    # approaches = Approach
    # lawyers = MemberLawyer
    # trainees = MemberTrainee
    # interns = MemberIntern

    class Meta:
        verbose_name = "área de atuação"
        verbose_name_plural = "áreas de atuação"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def members(self):
        return sorted(chain(self.lawyers.all(), self.trainees.all(), self.interns.all()), key=lambda m: m.member.first_name)


class SpecializationSector(Model):
    name = CharField("Nome", max_length=50, unique=True)
    description = RichTextField("Descrição", blank=True, null=True)
    picture = ImageField("Capa da página", blank=True,
                         null=True, upload_to=upload_to)

    # approaches = Approach
    # lawyers = MemberLawyer
    # trainees = MemberTrainee
    # interns = MemberIntern

    class Meta:
        verbose_name = "setor de especialização"
        verbose_name_plural = "setores de especialização"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def members(self):
        return sorted(chain(self.lawyers.all(), self.trainees.all(), self.interns.all()), key=lambda m: m.member.first_name)


class Approach(Model):
    text = TextField("Texto")

    practice_area = ForeignKey(
        PracticeArea, CASCADE, verbose_name="Área de Atuação", related_name="approaches")

    class Meta:
        verbose_name = "solução"
        verbose_name_plural = "soluções"
        unique_together = ("practice_area", "text")
        ordering = ("pk", )

    def __str__(self):
        return self.text


class ApproachSector(Model):
    text = TextField("Texto")

    specialization_sector = ForeignKey(
        SpecializationSector, CASCADE, verbose_name="Setor de Especialização", related_name="approaches", null=True)

    class Meta:
        verbose_name = "solução"
        verbose_name_plural = "soluções"
        unique_together = ("specialization_sector", "text")

    def __str__(self):
        return self.text


class Language(Model):
    name = CharField("Nome", max_length=50, unique=True)

    # lawyers = MemberLawyer

    class Meta:
        verbose_name = "idioma"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Award(Model):
    picture = ImageField("Imagem", blank=True, null=True, upload_to=upload_to)
    publication_date = DateField("Data de Publicação", default=datetime.now)
    title = CharField("Título", max_length=200, default="")
    description = RichTextUploadingField(
        "Descrição", default="", max_length=100)
    is_highlight = BooleanField("Em Destaque", default=False)

    class Meta:
        verbose_name = "prêmio"
        ordering = ["-is_highlight"]

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        highlighted_awards_limit = 3
        highlighted_awards = Award.objects.filter(is_highlight=True)
        if self.is_highlight and \
                highlighted_awards.filter(id=self.id).count() == 0 and \
                highlighted_awards.count() >= highlighted_awards_limit:
            raise ValidationError("Não pode haver mais de {} prêmios em destaque".format(
                highlighted_awards_limit))


class Partner(Model):
    logo_footer = ImageField(
        "Logo para footer", upload_to=upload_to, blank=True, null=True)
    logo_normal = ImageField(
        "Logo para página de quem somos", upload_to=upload_to, blank=True, null=True)
    site = URLField("Site", default="", blank=True, null=True)

    class Meta:
        verbose_name = "parceiro"

    def __str__(self):
        return f"Parceiro {self.id} - {self.site}"


class Affiliate(Model):
    logo_footer = ImageField(
        "Logo para footer", upload_to=upload_to, blank=True, null=True)
    logo_normal = ImageField(
        "Logo para página de quem somos", upload_to=upload_to, blank=True, null=True)
    site = URLField("Site", default="", blank=True, null=True)

    class Meta:
        verbose_name = "afiliado"

    def __str__(self):
        return f"Afiliado {self.id} - {self.site}"


# def __str__(self):
#   super(Partner, self).__str__()


class Office(Model):
    country = CharField("País", max_length=50, default="Brasil", blank=True)
    state = CharField("Estado", max_length=50, default="", blank=True)
    city = CharField("Cidade", max_length=50, default="", blank=True)
    neighborhood = CharField("Bairro", max_length=50, default="", blank=True)
    address = CharField("Endereço", max_length=200, default="", blank=True)
    gmaps_iframe = CharField(
        "Iframe Embbedado do Google", max_length=500, default="", blank=True)
    postcode = CharField("CEP", max_length=10, default="", blank=True)
    phone = CharField("Telefone", max_length=19, default="", blank=True)
    email = CharField("E-mail", max_length=50, default="", blank=True)
    is_parent = BooleanField("Matriz", default=False)
    office_order = PositiveSmallIntegerField("Ordem de exibição", default=99)

    class Meta:
        verbose_name = "escritório"
        ordering = ["-is_parent", "office_order"]

    def __str__(self):
        return "{} - {}".format(self.city, self.address)


class OpportunityRole(Model):
    name = CharField("Nome do Cargo", max_length=255)
    role_type = CharField(
        "Tipo", max_length=255, null=True, blank=True, unique=True
    )

    class Meta:
        verbose_name = "cargo"
        verbose_name_plural = "cargos"

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.name == 'Advogado':
                self.role_type = 'LAWYER'
            elif self.name == 'Estagiário':
                self.role_type = 'INTERN'
            elif self.name == 'Trainee':
                self.role_type = 'TRAINEE'
            else:
                self.role_type = self.name.upper()
        else:
            if self.role_type not in ['LAWYER', 'INTERN', 'TRAINEE']:
                self.role_type = self.name.upper()
            else:
                raise Exception('Não é possível, atualizar este cargo')
        super(OpportunityRole, self).save(*args, **kwargs)


class Opportunity(Model):
    ROLE_CHOICES = (
        ('LAWYER', 'Advogado'),
        ('INTERN', 'Estagiário'),
        ('TRAINEE', 'Trainee'),
    )
    LOCAL_CHOICES = (
        ('RC', 'Recife-PE'),
        ('SL', 'Salvador-BA'),
        ('BS', 'Brasília-DF'),
        ('SP', 'São Paulo-SP'),
    )
    active = BooleanField("Ativa", default=True)
    title = CharField("Título", max_length=200, default="")
    role = ForeignKey(
        OpportunityRole, verbose_name="Cargo", null=True, on_delete=PROTECT,
        blank=True, default=None
    )
    city = CharField("Cidade", max_length=20,
                     choices=LOCAL_CHOICES, default="RC")
    description_short = TextField("Descrição Curta", default="")
    description = RichTextUploadingField(
        "Descrição", default="", max_length=3000)
    requirements = RichTextUploadingField(
        "Requisitos", default="", max_length=3000)
    spots = IntegerField("Vagas", default=0)

    def display_city(self):
        return dict(Opportunity.LOCAL_CHOICES)[self.city]

    def display_role(self):
        return dict(Opportunity.ROLE_CHOICES)[self.role]

    class Meta:
        verbose_name = "oportunidade"

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        return self.spots > 0

    @property
    def related_applications(self):
        return self.opportunity.related_applications


class PublicationType(Model):
    # Tipos de Publicações e seus IDs
    PRESS = 1
    ARTICLE = 2
    INFORMATIVE = 3

    name = CharField("Nome", max_length=50, default="")

    class Meta:
        verbose_name = "tipo de publicação"
        verbose_name_plural = "tipos de publicação"

    def __str__(self):
        return self.name


class Publication(Model):
    creation_date = DateTimeField("Data de Criação", default=datetime.now)
    title = CharField("Título", max_length=200, default="")
    title_internal = CharField(
        "Título Interno", max_length=50, blank=True, null=True)
    description_short = TextField("Descrição Curta", default="")
    description = TextField("Descrição", blank=True, null=True)
    picture = ImageField("Capa da publicação", blank=True,
                         null=True, upload_to=upload_to)
    author = CharField("Autor", max_length=100, default="")
    vehicle = CharField("Veículo", max_length=100, blank=True, null=True)
    file = FileField("Anexo PDF", max_length=50, default="",
                     blank=True, null=True, upload_to=upload_to)

    related_practice_areas = ManyToManyField(
        PracticeArea, verbose_name="Áreas de Atuação Relacionadas", related_name="related_publication_areas", blank=True)
    related_specialization_sector = ManyToManyField(
        SpecializationSector, verbose_name="Setores de Especialização Relacionados", related_name="related_publication_sectors", blank=True)

    type = ForeignKey(PublicationType, PROTECT,
                      verbose_name="Tipo de Publicação", related_name="publications")
    related_members = ManyToManyField(
        "members.Member", verbose_name="Membros Relacionados", related_name="related_publications", blank=True)
    content = RichTextField(blank=True)

    class Meta:
        verbose_name = "publicação"
        verbose_name_plural = "publicações"
        ordering = ["-creation_date"]

    def __str__(self):
        return "{}: {}".format(self.type.name, self.title)


class Event(Model):
    date = DateField("Data")
    time = TimeField("Horário", blank=True, null=True)
    description_short = TextField("Descrição Curta", default="")
    country = CharField("País", max_length=2, blank=True, null=True)
    city = CharField("Cidade", max_length=50, blank=True, null=True)
    address = CharField("Endereço", max_length=200, default="")
    picture = ImageField("Capa do evento", blank=True,
                         null=True, upload_to=upload_to)
    related_events_lawyers = ManyToManyField(
        "members.MemberLawyer", verbose_name="Advogados Relacionados", related_name="related_events_lawyers", blank=True)
    related_events_trainees = ManyToManyField(
        "members.MemberTrainee", verbose_name="Trainees Relacionados", related_name="related_events_trainees", blank=True)
    related_practice_areas = ManyToManyField(
        PracticeArea, verbose_name="Áreas de Atuação Relacionadas", related_name="related_event_areas", blank=True)
    related_specialization_sector = ManyToManyField(
        SpecializationSector, verbose_name="Setores de Especialização Relacionados", related_name="related_event_sectors", blank=True)

    content = RichTextField(blank=True, null=True, default="")
    sympla_grid = TextField("Sympla - Grid de ingressos", blank=True, null=True)
    sympla_button = TextField("Sympla - Botão de ingressos", blank=True, null=True)

    class Meta:
        verbose_name = "evento"
        ordering = ["-date", "-time"]

    def __str__(self):
        return self.description_short

    def save(self, *args, **kwargs):
        print(self)
        super(Event, self).save(*args, **kwargs)


class SocialEntity(Model):
    name = CharField("Nome", max_length=50, default="")
    picture = ImageField("Logo da entidade social",
                         blank=True, null=True, upload_to=upload_to)
    description = TextField("Descrição", default="")
    site = URLField("Site", default="")

    class Meta:
        verbose_name = "entidade social"
        verbose_name_plural = "entidades sociais"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Contact(Model):
    name = CharField("Nome", max_length=50, default="")
    email = CharField("E-mail", max_length=70, default="")
    telefone = CharField("Telefone", max_length=20, default="")
    message = TextField("Mensagem", blank=True, null=True)
    created_at = DateTimeField("Entrou em contato em", default=datetime.now)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.localtime(timezone.now())
        super(Contact, self).save(*args, **kwargs)


class Values(Model):
    title = CharField("Titulo", max_length=200, default="")
    description = TextField("Descrição", default="")

    class Meta:
        verbose_name = "valor"
        verbose_name_plural = "valores"

    def __str__(self):
        return self.title
