from django.db import models

from members.models import Member, MemberAdministrativeStaff, MemberIntern, MemberLawyer, MemberTrainee, MemberType


class ProxyMemberManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.member_type)


class ProxyIntern(Member):
    member_type = MemberType.INTERN

    objects = ProxyMemberManager()

    class Meta:
        proxy = True
        verbose_name = MemberIntern._meta.verbose_name
        verbose_name_plural = MemberIntern._meta.verbose_name_plural


class ProxyLawyer(Member):
    member_type = MemberType.LAWYER

    objects = ProxyMemberManager()

    class Meta:
        proxy = True
        verbose_name = MemberLawyer._meta.verbose_name
        verbose_name_plural = MemberLawyer._meta.verbose_name_plural


class ProxyTrainee(Member):
    member_type = MemberType.TRAINEE

    objects = ProxyMemberManager()

    class Meta:
        proxy = True
        verbose_name = MemberTrainee._meta.verbose_name
        verbose_name_plural = MemberTrainee._meta.verbose_name_plural


class ProxyAdministrativeStaff(Member):
    member_type = MemberType.ADMINISTRATIVE_STAFF

    objects = ProxyMemberManager()

    class Meta:
        proxy = True
        verbose_name = MemberAdministrativeStaff._meta.verbose_name
        verbose_name_plural = MemberAdministrativeStaff._meta.verbose_name_plural
