# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Gestion de Location",
    "summary": "Gestion de Location",
    "author": "HATECH",
    "website": "www.hornafricatech.com",
    "category": "Custom Application",
    "version": "14.0",
    "license": "AGPL-3",
    "depends": ['base', 'mail','account'],
    "data": [
        'views/main_menu_view.xml',
        'views/gestion_logement.xml',
        'views/projet_logement.xml',
        'views/type_propriete.xml',
        'views/gestion_avenant.xml',
        'security/ir.model.access.csv',
        # 'views/email_template.xml',

    ],
    'images': [
        'static/description/icon.png',
    ],

    'license': 'AGPL-3',
    'installable': True,
    "application": True,
    "development_status": "Beta",
    "maintainers": ["Horn Africa Technology"],
}
