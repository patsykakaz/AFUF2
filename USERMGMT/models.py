#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#, editable=False)
    nom = models.CharField(max_length=255, blank=False)
    prenom = models.CharField(max_length=255, blank=False)
    date_naissance = models.CharField(max_length=255, blank=False, null=True, verbose_name='date de naissance')
    adresse = models.CharField(max_length=255, verbose_name='adresse postale complète')
    email = models.EmailField(blank=False, verbose_name='adresse email')
    tel = models.CharField(max_length=255, blank=False, verbose_name='téléphone')
    # photo = FileField(verbose_name=_("photo"), upload_to=upload_to("USERMGMT.Profile.photo", "profile"),format="Image", max_length=255, null=True, blank=True)
    annee_ECN = models.CharField(max_length=255, blank=False, verbose_name='Année du concours de l\'ECN')
    semestre = models.CharField(max_length=255, blank=True, verbose_name='semestre commencé en novembre 2016')
    annee_debut_post_internat = models.CharField(max_length=255, blank=False,verbose_name='année du début de post-internat', help_text='Année, prévisible ou effective, de début de post-internat')
    region_choices = (
        ('Ile de France','Ile de France'),
        ('Est', 'Est'),
        ('Nord', 'Nord'),
        ('Ouest', 'Ouest'),
        ('Rhône-Alpes', 'Rhône-Alpes'),
        ('Sud', 'Sud'),
        ('Sud-Ouest', 'Sud-Ouest'),
        ('DOM-TOM', 'DOM-TOM'),
    )
    inter_region = models.CharField(max_length=255, blank=False, choices=region_choices, verbose_name='inter-région de formation') #, help_text='Votre inter-région de formation (DOM-TOM, Est, Ile de France, Nord, Ouest, Rhône-Alpes, Sud, Sud-Ouest) ?'
    service_actuel = models.CharField(max_length=255, blank=False, verbose_name='votre service actuel', help_text='Précisez votre centre, le service, le chef de service et la ville')
    diplome_choices = (
        ('Non','Non'),
        ('Pas intéressé', 'Pas intéressé'),
        ('En cours', 'En cours'),
        ('Validé', 'Validé'),
    )
    diplome_master_2 = models.CharField(max_length=255, null=True, blank=False, verbose_name='Master 2', choices=diplome_choices, default='')
    diplome_DESC_andrologie = models.CharField(verbose_name='DESC d\'andrologie', max_length=255, choices=diplome_choices, null=True, blank=False, default='')
    diplome_DESC_oncologie_1 = models.CharField(verbose_name='DESC d\'oncologie option médicale', max_length=255, choices=diplome_choices, null=True, blank=False, default='')
    diplome_DESC_oncologie_2 = models.CharField(verbose_name='DESC d\'oncologie option chirurgicale', max_length=255, choices=diplome_choices, null=True, blank=False, default='')
    diplome_autre = models.TextField(verbose_name='Autres diplomes', null=True, blank=True, default='', help_text='Si oui, précisez.')
    status_actuel_choices = (
        ('Interne DES','Interne DES'),
        ('Interne titre étranger', 'Interne titre étranger'),
        ('Assistant', 'Assistant'),
        ('CCA', 'CCA'),
        ('Autre', 'Autre'),
    )
    statut_actuel = models.CharField(max_length=255, choices=status_actuel_choices, null=True, blank=False)
    statut_autre = models.CharField(max_length=255, null=True, blank=True, help_text='Précisez, si autre statut (médaille d\'or, année de césure, mobilité, année recherche ...)')
    justificatif_scolarite = models.FileField(verbose_name='Pièce justificative',upload_to='uploads/justificatifs/', blank=False, help_text='Certificat de scolarité (si interne), feuille de paie (si CCA) ou attestation du chef de service')
    # envoie boite mail
    choix_adhesion = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        print 'saving profile for : ' + self.email
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()