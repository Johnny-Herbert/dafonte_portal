from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import datetime

from portal.models import (
    PracticeArea, Publication, Event, SpecializationSector
)
from portal.views import PageView
from members.models import Member, MemberLawyer, MemberType
from members.utils import get_initials


class MemberListView(PageView):
    template_name = "member-list.html"
    slug = "member-list"

    def get(self, request, *args, **kwargs):
        super(MemberListView, self).get(request, *args, **kwargs)
        context = self.get_context_data(object=self.object)

        type_staff = [MemberType.ADMINISTRATIVE_STAFF]
        type_all = [MemberType.TRAINEE, MemberType.INTERN, MemberType.LAWYER,
                    MemberType.ADMINISTRATIVE_STAFF]
        type_interns = [MemberType.TRAINEE, MemberType.INTERN]
        type_lawyer = [MemberType.LAWYER]

        should_filter_by_initial = False
        if request.GET.get("filter-by-initial", None) == "true":
            should_filter_by_initial = True

        member_initial = ""
        initials = []
        search_term = request.GET.get("search-term", "")
        filter_member_type = request.GET.get("filter-member-type", "")
        filter_practice_area = request.GET.get("filter-practice-area", "all")
        filter_specialization_sector = request.GET.get(
            "filter-specialization-sector", "all"
        )

        filtered_members = Member.objects.all()

        if search_term:
            filter_member_type = "all"

        if filter_member_type == "ti":
            filtered_members = filtered_members.filter(type__in=type_interns)
        elif filter_member_type == "staff":
            filtered_members = filtered_members.filter(type__in=type_staff)
        elif filter_member_type in ["", "all"]:
            filtered_members = filtered_members.filter(type__in=type_all)
        else:
            filtered_members = filtered_members.filter(type__in=type_lawyer)

        # filtra por area de atuacao ou setor de especialização
        if filter_member_type == "lawyer":
            if filter_practice_area != "all":
                filtered_members = filtered_members.filter(
                    lawyer__practice_areas=filter_practice_area
                )
            elif filter_specialization_sector != "all":
                filtered_members = filtered_members.filter(
                    lawyer__specialization_sector=filter_specialization_sector
                )

        # fix pesquisa por nome
        initials_bkp = filtered_members.all()

        if should_filter_by_initial:
            member_initial = request.GET.get("member-initial", "")
            search_term = ""
            filtered_members = filtered_members.filter(
                first_name__istartswith=member_initial
            )
        elif search_term != "":
            filter_practice_area = "all"
            filter_specialization_sector = "all"
            filtered_members = filtered_members.filter(
                Q(first_name__unaccent__icontains=search_term) |
                Q(last_name__unaccent__icontains=search_term)
            )

        practice_areas = PracticeArea.objects.all()
        specialization_sectors = SpecializationSector.objects.all()

        if should_filter_by_initial or search_term != "":
            initials = get_initials(initials_bkp)
        else:
            initials = get_initials(filtered_members)

        search_term = ""

        context.update(
            members=filtered_members,
            selected_initial=member_initial,
            search_term=search_term,
            filter_member_type=filter_member_type,
            filter_practice_area=filter_practice_area,
            filter_specialization_sector=filter_specialization_sector,
            practice_areas=practice_areas,
            specialization_sectors=specialization_sectors,
            initials=initials
        )

        return self.render_to_response(context)


class MemberDetailView(PageView):
    template_name = "member-detail.html"
    slug = "member-detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member_id = self.kwargs.get("member_id", None)

        if self.object.id is not None:
            member = get_object_or_404(MemberLawyer, id=member_id)
            context.update(member=member)

            # member é um Lawyer e member.member um member
            latest_publications = Publication.objects.filter(
                related_members__id=member.member.id
            )

            # como a procura é por lawyer podemos usar só member.
            latest_events = Event.objects.filter(
                related_events_lawyers__id=member.id,
                date__gte=datetime.today()
            ).order_by('date')[:6]

            if len(latest_events) == 0:
                print('empty query')
                latest_events = Event.objects.filter(
                    related_events_lawyers__id=member.id
                ).order_by('-date')[:6]

            context.update(
                latest_publications=latest_publications,
                latest_events=latest_events
            )
        return context
