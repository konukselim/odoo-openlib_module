# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    author = fields.Boolean("Is a Book Author", default=False)
    publisher = fields.Boolean("Is a Book Publisher", default=False)

    written_books = fields.Many2many('openlib.book',
        string="Books", readonly=True)
    published_books = fields.Many2many('openlib.book',
        string="Books", readonly=True)