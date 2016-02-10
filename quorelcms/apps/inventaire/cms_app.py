# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

#from .menu import DocumentSubMenu


class inventaireApp(CMSApp):
    name = _('inventaire')
    urls = ['quorelcms.apps.inventaire.urls', ]
    app_name = "inventaire"
   # menus = [DocumentSubMenu, ]

apphook_pool.register(inventaireApp)