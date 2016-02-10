# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import Document


class InventaireSubMenu(CMSAttachMenu):

    name = _("Inventaire Sous-Menu")

    def get_nodes(self, request):
        nodes = []

        # for document in Document.objects.order_by('nom_document').all():

        #     node = NavigationNode(
        #         mark_safe(document.nom_document),
        #         document.get_absolute_url(),
        #         document.pk,
        #     )

        #     nodes.append(node)

        return nodes

menu_pool.register_menu(InventaireSubMenu)