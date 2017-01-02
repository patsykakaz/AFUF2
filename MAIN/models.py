# #-*- coding: utf-8 -*-

# from __future__ import unicode_literals

# from django.db import models
# from django.contrib.sites.models import *
# from django.utils.translation import ugettext, ugettext_lazy as _

# from settings import MEDIA_ROOT
# from mezzanine.pages.models import Page
# from mezzanine.core.models import RichText
# from mezzanine.core.fields import RichTextField, FileField
# from mezzanine.utils.models import upload_to
# from mezzanine.utils.sites import current_site_id, current_request



# class Category(Page):
#     order = models.IntegerField(default=0, verbose_name='ordre de priorité')
#     illustration = FileField(verbose_name=_("Illustration"), upload_to=upload_to("MAIN.Category.illustration", "category"),format="Image", max_length=255, null=True, blank=True)
#     logo_parrain = FileField(verbose_name=_("Logo Parrain"), upload_to=upload_to("MAIN.Category.logo_parrain", "logo_parrain"),format="Image", max_length=255, null=True, blank=True)
#     presentation_parrain =RichTextField(_("Présentation parrain"),blank=True)

#     def save(self, *args, **kwargs):
#         self.in_menus = []
#         try:
#             self.parent = Page.objects.get(title='CATEGORIES')
#         except: 
#             pass
#         super(Category, self).save(*args, **kwargs)

# class Product(Page):
#     """
#         title = company name
#         richText = description
#     """
#     cat_product = models.ForeignKey('Category',null=True,blank=True, verbose_name='category for product')
#     baseline = models.CharField(max_length=255,blank=True)
#     productName = models.CharField(max_length=255)
#     presentation_product = RichTextField(_("Content"),blank=True)
#     town = models.CharField(max_length=255,blank=True)
#     price = models.CharField(max_length=255,blank=True)
#     discount = models.CharField(max_length=255,blank=True)
#     illustration = FileField(verbose_name=_("illustration principale du produit"),
#         upload_to=upload_to("MAIN.Product.illustration", "illustration"),
#         format="Image", max_length=255, null=True, blank=True)
#     illustration2 = FileField(upload_to=upload_to("MAIN.Product.illustration", "illustration 2"),
#         format="Image", max_length=255, null=True, blank=True)
#     illustration3 = FileField(upload_to=upload_to("MAIN.Product.illustration", "illustration 3"),
#         format="Image", max_length=255, null=True, blank=True)
#     illustration4 = FileField(upload_to=upload_to("MAIN.Product.illustration", "illustration 4"),
#         format="Image", max_length=255, null=True, blank=True)
#     presentation_sup = RichTextField(_("Presentation Start-up"),blank=True)
#     logo = FileField(verbose_name=_("logo"),
#         upload_to=upload_to("MAIN.Product.illustration", "logo Start-Up"),
#         format="Image", max_length=255, null=True, blank=True)
#     team_pic = FileField(upload_to=upload_to("MAIN.Product.illustration", "photo Team "),format="Image", max_length=255, null=True, blank=True)
#     mainLink = models.URLField(null=True,blank=False)
#     website = models.URLField(null=True,blank=True)
#     facebook = models.URLField(null=True,blank=True)
#     twitter = models.URLField(null=True,blank=True)
#     instagram = models.URLField(null=True,blank=True)

#     class Meta:
#         verbose_name='PRODUIT'
#         ordering = ['title']

#     def save(self, *args, **kwargs):
#         self.in_menus = []
#         try:
#             self.parent = Page.objects.get(title='PRODUITS')
#         except: 
#             pass
#         super(Product, self).save(*args, **kwargs)





