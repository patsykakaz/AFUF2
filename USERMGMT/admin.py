#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

# from mezzanine.blog.admin import BlogPostAdmin
# from mezzanine.blog.models import BlogPost


# profile_fieldsets = deepcopy(PageAdmin.fieldsets)
# profile_fieldsets[0][1]["fields"].insert(-1, "user")
# profile_fieldsets[0][1]["fields"].insert(-1, "nom")
# profile_fieldsets[0][1]["fields"].insert(-1, "prenom")
# profile_fieldsets[0][1]["fields"].insert(-1, "date_naissance")
# profile_fieldsets[0][1]["fields"].insert(-1, "adresse")
# profile_fieldsets[0][1]["fields"].insert(-1, "email")
# profile_fieldsets[0][1]["fields"].insert(-1, "tel")
# profile_fieldsets[0][1]["fields"].insert(-1, "annee_ECN")
# profile_fieldsets[0][1]["fields"].insert(-1, "semestre")
# profile_fieldsets[0][1]["fields"].insert(-1, "annee_debut_post_internat")
# profile_fieldsets[0][1]["fields"].insert(-1, "inter_region")
# profile_fieldsets[0][1]["fields"].insert(-1, "service_actuel")
# profile_fieldsets[0][1]["fields"].insert(-1, "diplome_master_2")
# profile_fieldsets[0][1]["fields"].insert(-1, "diplome_DESC_andrologie")
# profile_fieldsets[0][1]["fields"].insert(-1, "diplome_DESC_oncologie")
# profile_fieldsets[0][1]["fields"].insert(-1, "diplome_autre")
# profile_fieldsets[0][1]["fields"].insert(-1, "statut_actuel")
# profile_fieldsets[0][1]["fields"].insert(-1, "statut_autre")
# profile_fieldsets[0][1]["fields"].insert(-1, "justificatif_scolarite")
# profile_fieldsets[0][1]["fields"].insert(-1, "choix_adhesion")
# class ProfileAdmin(PageAdmin):
#     fieldsets = profile_fieldsets

admin.site.register(Profile)







