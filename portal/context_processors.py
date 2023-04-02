import string

from django.conf import settings
from portal.models import Award, Affiliate, Partner, Office, Opportunity
from members.models import MemberIntern, MemberLawyer, MemberTrainee


def base(request):
    initials = [
        dict(value=i, disabled=(
            MemberLawyer.objects.filter(member__first_name__istartswith=i).count() == 0 and
            MemberIntern.objects.filter(member__first_name__istartswith=i).count() == 0 and
            MemberTrainee.objects.filter(member__first_name__istartswith=i).count() == 0
            ))
        for i in list(string.ascii_uppercase)
    ]

    awards = Award.objects.all()
    partners = Partner.objects.all()
    affiliates = Affiliate.objects.all()
    offices = Office.objects.all()
    opportunities = Opportunity.objects.filter(spots__gt=0)

    return dict(
            initials=initials,
            awards=awards,
            partners=partners,
            affiliates=affiliates,
            offices=offices,
            open_opportunities=opportunities
    )


def ga_tracking_id(request):
    """ get google analytics tracking id """
    return {'ga_tracking_id': settings.GA_TRACKING_ID}
