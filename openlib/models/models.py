# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'openlib.book'

    name = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN")
    publication_date = fields.Date()