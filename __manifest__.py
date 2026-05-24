# -*- coding: utf-8 -*-
{
    'name': 'Orden de Nombre en Contactos',
    'version': '19.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Corrige el orden de los campos de nombre: Nombre → Segundo Nombre → Apellido.',
    'description': """
Módulo que reordena los campos de nombre en el formulario de contactos.
Orden correcto: Nombre → Segundo Nombre (Middle Name) → Apellido → Segundo Apellido.

Requiere los módulos OCA: partner_firstname y partner_middlename (Odoo 19).
    """,
    'author': 'Brooks González / Antigravity',
    'depends': ['partner_firstname', 'partner_middlename'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
