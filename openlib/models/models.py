# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'openlib.book'

    name = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN")
    publication_date = fields.Date()

class BookGenre(models.Model):
    _name = 'openlib.genre'
    
    name = fields.Char(string="Genre", required=True)

class Language(models.Model):
    _name = 'openlib.language'

    name = fields.Char(string="Language", required=True)