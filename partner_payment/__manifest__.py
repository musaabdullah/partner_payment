# -*- coding: utf-8 -*-
{
    'name': "Partner Payments | Open Payment from partner",

    'summary': """
        This module is allow to open payment from customer from.""",
    'description': """
       This module is allow to open payment from customer from.
    """,

    'author': "Musa Abdullah",
    'category': 'Uncategorized',
    'version': '16.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "images": ["static/description/bill.jpeg"],
}
