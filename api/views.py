from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from itertools import chain


from members.models import Member, MemberLawyer, MemberAdministrativeStaff, MemberTrainee, MemberIntern, JobTitle
import pdb
@api_view(["GET"])
def lawyerList(request):
    memberslaw = MemberLawyer.objects.all().order_by("member_id").values()
    members = Member.objects.filter(type_id=1).order_by("-id").values()
    
    advogados = []
    for law in memberslaw:
        advogados.append(law)
        for member in members:
            if law["member_id"] == member["id"]:
                member["photo"] = 'https://dafonte-site-arquivos.fra1.digitaloceanspaces.com/'+member["photo"]
                member["type_id"] = "Advogado(a)"
                law.update(member)
    pdb.set_trace()
    return Response(advogados)


@api_view(["GET"])
def admList(request):
    membersadm = MemberAdministrativeStaff.objects.all().order_by("member_id").values()
    members = Member.objects.filter(type_id=2).order_by("-id").values()
    cargos = JobTitle.objects.all().order_by("id").values()

    administrativo = []
    for adm in membersadm:
        for cargo in cargos:
            if adm["job_title_id"] == cargo["id"]:
                adm["job_title_id"] = cargo["name"]
                adm.update(adm)
        administrativo.append(adm)
        for member in members:
            if adm["member_id"] == member["id"]:
                member["photo"] = 'https://dafonte-site-arquivos.fra1.digitaloceanspaces.com/'+member["photo"]
                member["type_id"] = "Administrativo"
                adm.update(member)
    return Response(administrativo)


@api_view(["GET"])
def treineeList(request):
    memberstreinee = MemberTrainee.objects.all().order_by("member_id").values()
    members = Member.objects.filter(type_id=3).order_by("-id").values()

    treinees = []
    for treinee in memberstreinee:
        treinees.append(treinee)
        for member in members:
            if treinee["member_id"] == member["id"]:
                member["photo"] = 'https://dafonte-site-arquivos.fra1.digitaloceanspaces.com/'+member["photo"]
                member["type_id"] = "Treinee"
                treinee.update(member)
    return Response(treinees)


@api_view(["GET"])
def internList(request):

    memberintern = MemberIntern.objects.all().order_by("member_id").values()
    members = Member.objects.filter(type_id=4).order_by("-id").values()

    estags = []
    for estag in memberintern:
        estags.append(estag)
        for member in members:
            if estag["member_id"] == member["id"]:
                member["photo"] = 'https://dafonte-site-arquivos.fra1.digitaloceanspaces.com/'+member["photo"]
                member["type_id"] = "Interno"
                estag.update(member)
    return Response(estags)