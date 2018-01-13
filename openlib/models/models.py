# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'openlib.book'

    name = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN")
    publication_date = fields.Date()
    genre = fields.Many2one('openlib.genre',
        ondelete='set null', string="Genre", index=True)
    language = fields.Many2one('openlib.language',
        ondelete='set null', string="Language", index=True)

    author_id = fields.Many2one('res.partner', string="Author",
        domain=[('author', '=', True)])

    # instructor_id = fields.Many2one('res.partner', string="Instructor",
    #                                 domain=['|', ('instructor', '=', True),
    #                                         ('category_id.name', 'ilike', "Teacher")])

    # publisher_id = fields.Many2one('openlib.book_publisher',
    #     ondelete='cascade', string="Publisher", required=True)
    # author_ids = fields.Many2many('openlib.author', string="Authors")


class BookGenre(models.Model):
    _name = 'openlib.genre'
    
    name = fields.Char(string="Genre", required=True)

class Language(models.Model):
    _name = 'openlib.language'

    name = fields.Char(string="Language", required=True)