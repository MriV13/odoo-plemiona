{
    'name': 'Website - Plemiona',
    'version': '17.0.1.0.0',
    'depends': ['website'],
    'summary': ".",
    'description': """.""",
    'demo': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/world_world_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
{
    'name': 'Village Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/village_views.xml',  # Add the path to your XML file
    ],
    'application': True,
}