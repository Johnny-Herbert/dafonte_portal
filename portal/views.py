from datetime import datetime, date
from django.core.files import File
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext
from django.views import View
from django.views.generic import DetailView
from dateutil.relativedelta import relativedelta
import os
import requests

from portal.models import Award, Page, Event, Publication, PracticeArea, PublicationType, SocialEntity, SpecializationSector, SiteParameter
from portal.models import Contact, Values
from portal.forms import ContactForm


# class UploadedFilesView(View):
#   def dispatch(self, request, file_name, *args, **kwargs):
#     image_data = open("files/{}".format(file_name), "rb").read()
#     return HttpResponse(image_data)
#
#
class PageView(DetailView):
  model = Page
  fail_template_name = "page-object-not-found.html"
  slug = None

  def get_object(self, queryset=None):
    try:
      return Page.objects.get(slug=self.slug)
    except Page.DoesNotExist:
      return Page()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    if self.object.id is None:
      self.template_name = self.fail_template_name
      context.update(slug=self.slug)

    return context

class HomeView(PageView):
  template_name = "home.html"
  slug = "home"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    if self.object.id is not None:
      request_context = RequestContext(self.request)
      awards = request_context.get("awards", Award.objects.all())
      highlighted_awards = awards.filter(is_highlight=True)
      latest_events = Event.objects.filter(date__gte=datetime.today()).order_by('date')[:6]
      latest_publications = Publication.objects.all()[:3]
      practice_areas = PracticeArea.objects.all()
      social_entities = SocialEntity.objects.all()
      specialization_sector = SpecializationSector.objects.all()

      context.update(
          highlighted_awards=highlighted_awards,
          latest_events=latest_events,
          latest_publications=latest_publications,
          practice_areas=practice_areas,
          social_entities=social_entities,
          specialization_sector=specialization_sector,
      )

    return context


class PracticeAreaListView(PageView):
  template_name = "practice-area-list.html"
  slug = "practice-area-list"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    if self.object.id is not None:
      request_context = RequestContext(self.request)
      practice_areas = PracticeArea.objects.all()
      latest_events = Event.objects.filter(date__gte=datetime.today()).order_by('date')[:6]
      latest_publications = Publication.objects.all()[:3]
      social_entities = SocialEntity.objects.all()
      specialization_sector = SpecializationSector.objects.all()

      context.update(
          practice_areas=practice_areas,
          specialization_sector = specialization_sector,
          latest_events=latest_events,
          latest_publications=latest_publications,
          social_entities=social_entities
      )

    return context

class SpecializationSectorDetailView(PageView):
  template_name = "specialization-sector-detail.html"
  slug = "specialization-sector-detail"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    sector_id = self.kwargs.get("sector_id", None)
    latest_events = Event.objects.filter(date__gte=datetime.today()).order_by('date')[:6]
    latest_publications = Publication.objects.all()[:3]

    if self.object.id is not None:
      specialization_sector = SpecializationSector.objects.get(id=sector_id)
      context.update(
          practice_area=specialization_sector,
          latest_events=latest_events,
          latest_publications=latest_publications,
      )

    return context


class PracticeAreaDetailView(PageView):
  template_name = "practice-area-detail.html"
  slug = "practice-area-detail"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    practice_id = self.kwargs.get("practice_id", None)

    if self.object.id is not None:
      practice_area = PracticeArea.objects.get(id=practice_id)

      latest_events = Event.objects.all().filter(related_practice_areas__pk = practice_area.pk, date__gte=datetime.today()).order_by('date')[:6]
      latest_publications = Publication.objects.all().filter(related_practice_areas__pk = practice_area.pk)[:3]

      context.update(
          practice_area=practice_area,
          latest_events=latest_events,
          latest_publications=latest_publications,
      )

    return context


class WhoWeAreView(PageView):
  template_name = "who-we-are.html"
  slug = "who-we-are"

class ComplianceView(PageView):
  template_name = "compliance.html"
  slug = "compliance"

class CollaborationView(PageView):
  template_name = "collaboration.html"
  slug = "collaboration"

class CultureView(PageView):
  template_name = "culture.html"
  slug = "culture"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update(
      values=Values.objects.all()
    )

    return context

class AwardListView(PageView):
  template_name = "award-list.html"
  slug = "award-list"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update(
      awards=Award.objects.all()
    )

    return context


class PressListView(PageView):
  template_name = "press-list.html"
  slug = "press-list"

  def get(self, request, *args, **kwargs):
    super(PressListView, self).get(request, *args, **kwargs)
    context = super().get_context_data(**kwargs)
    search_term = request.GET.get("search-term", "")

    presses = Publication.objects.filter(type__id=PublicationType.PRESS)

    if search_term:
      presses = presses.filter(title__icontains=search_term)
    
    presses = presses.distinct()

    paginator = Paginator(presses, 10)
    page = request.GET.get("page", 1)
    page_presses = paginator.get_page(page)

    context.update(
        presses=page_presses,
        current_page=page,
        num_pages=paginator.num_pages,
        search_term=search_term
    )

    return self.render_to_response(context)

class PressDetailView(PageView):
  template_name = "press-detail.html"
  slug="press-detail"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    press_pk = self.kwargs.get("press_pk", None)

    if self.object.id is not None:
      press = get_object_or_404(Publication, id=press_pk)
      context.update(press=press)
    return context

class ArticleListView(PageView):
  template_name = "article-list.html"
  slug = "article-list"

  def get(self, request, *args, **kwargs):
    super(ArticleListView, self).get(request, *args, **kwargs)
    context = super().get_context_data(**kwargs)
    search_term = request.GET.get("search-term", "")

    articles = Publication.objects.filter(type__id=PublicationType.ARTICLE)

    if search_term:
      articles = articles.filter(title__icontains=search_term)

    paginator = Paginator(articles,10)
    page = request.GET.get("page", 1)
    page_articles = paginator.get_page(page)

    context.update(
        articles=page_articles,
        current_page=page,
        num_pages=paginator.num_pages,
        search_term=search_term
    )

    return self.render_to_response(context)

class ArticleDetailView(PageView):
  template_name = "article-detail.html"
  slug="article-detail"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    article_pk = self.kwargs.get("article_pk", None)

    if self.object.id is not None:
      article = get_object_or_404(Publication, pk=article_pk)
      context.update(article=article)
    return context

class EventListView(PageView):
  template_name = "event-list.html"
  slug = "event-list"

  def get(self, request, *args, **kwargs):
    super(EventListView, self).get(request, *args, **kwargs)
    context = super().get_context_data(**kwargs)
    events = Event.objects.filter(date__gte=datetime.today())
    show_next_events_title = True
    # search = request.GET.get('search-term-string')
    date = request.GET.get('search-term-date')
    if(date):
        year = date.split('-')[0]
        month = date.split('-')[1]
        events = Event.objects.filter(date__month=month, date__year=year)
        show_next_events_title = False
    elif(len(events) == 0):
      show_next_events_title = False
      control = 0
      month_before = datetime.today()
      while(len(events) == 0 and control < 24):#Busca até dois anos atrás.
        month_before = month_before - relativedelta(months=+1)
        events = Event.objects.filter(date__gte=month_before)
        control = control + 1
    events = events.order_by('date')
    context.update(
        events=events,
        show_next_events_title=show_next_events_title,
    )
    return self.render_to_response(context)

class EventDetailView(PageView):
  template_name = "event-detail.html"
  slug="event-detail"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    event_pk = self.kwargs.get("event_pk", None)

    if self.object.id is not None:
      event = get_object_or_404(Event, id=event_pk)
      if event.date >= date.today():
        context.update(future=True)
      context.update(event=event)
    return context

class SocialResponsabilityView(PageView):
  template_name = "social-reponsability.html"
  slug = "social-reponsability"

  def get(self, request, *args, **kwargs):
    super(SocialResponsabilityView, self).get(request, *args, **kwargs)
    context = super().get_context_data(**kwargs)

    # header_presses = Publication.objects.filter(type__id=PublicationType.PRESS)[:3]
    social_entities = SocialEntity.objects.all()

    # paginator = Paginator(presses, 6)
    # page = request.GET.get("page", 1)
    # social_entities = paginator.get_page(page)

    # header_presses=header_presses,
    context.update(
        social_entities=social_entities,
    )
    # current_page=page

    return self.render_to_response(context)


class ContactView(PageView):
  template_name = "contact.html"
  slug = "contact"

  def get(self, request, *args, **kwargs):
    super(ContactView, self).get(request, *args, **kwargs)
    context = super().get_context_data(**kwargs)

    # header_presses = Publication.objects.filter(type__id=PublicationType.PRESS)[:3]
    events = Event.objects.filter(date__gte=datetime.today()).order_by('date')

    # paginator = Paginator(presses, 6)
    # page = request.GET.get("page", 1)
    # events = paginator.get_page(page)

    # header_presses=header_presses,
    context.update(
        events=events,
    )
    # current_page=page
    return self.render_to_response(context)

  def post(self, request, *args, **kwargs):
        super(ContactView, self).get(request, *args, **kwargs)
        context = super().get_context_data(**kwargs)
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(**form.cleaned_data)
            contact.save()
            context['contact_created'] = True
        return self.render_to_response(context)


class InstitutionalFolderView(View):
  def get(self, request, *args, **kwargs):

    from static.pdf.flip_html5 import flip_url
    from django.utils.translation import get_language

    flip_pt, flip_en = flip_url

    if get_language() == 'pt-br':
      flip = flip_pt
    if get_language() == 'en':
      flip = flip_en

    try:
      flip_url = requests.get(flip)
      if flip_url.status_code == 200:
        return redirect(flip)

    except:      
      param_name = 'institutional-folder'
      from django.views.static import serve
      try:
        param = SiteParameter.objects.get(name=param_name)
        filepath = param.file.url 
        return redirect(param.file.url)
      except SiteParameter.DoesNotExist:
        filepath = f'static/pdf/dafonte-folder-institucional-{flip}.pdf'
        return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


class CodeConductView(View):
    def get(self, request, *args, **kwargs):

        param_name = 'code-of-conduct'
        from django.views.static import serve
        try:
          param = SiteParameter.objects.get(name=param_name)
          filepath = param.file.url 
          from django.shortcuts import redirect
          
          return redirect(param.file.url)
        except SiteParameter.DoesNotExist:
          filepath = 'static/pdf/codigo-de-conduta-e-etica.pdf'
          return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

class PrivacyPolicy(View):
    def get(self, request, *args, **kwargs):

        param_name = 'privacy-policy'
        from django.views.static import serve
        try:
          param = SiteParameter.objects.get(name=param_name)
          filepath = param.file.url 
          from django.shortcuts import redirect
          
          return redirect(param.file.url)
        except SiteParameter.DoesNotExist:
          filepath = 'static/pdf/privacy-policy.pdf'
          return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

          

