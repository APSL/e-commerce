# -*- coding: utf-8 -*-
# © 2016 Andhitia Rama <andhitia.r@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Display Product UoM in e-commerce website",
    "version": "8.0.1.0.0",
    "author": "Andhitia Rama,Odoo Community Association (OCA)",
    "website": "https://opensynergy-indonesia.com",
    "license": "AGPL-3",
    "category": "Website",
    "depends": [
        "website_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/website_product.xml",
    ],
    "active": False,
    'installable': True
}
