# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    author = fields.Boolean("Author", default=False)
    publisher = fields.Boolean("Publisher", default=False)

    written_books = fields.Many2many('openlib.book',
        string="Books", readonly=True)
    published_books = fields.Many2many('openlib.book',
        string="Books2", readonly=True)
