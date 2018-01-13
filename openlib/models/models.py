# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Book(models.Model):
    _name = 'openlib.book'

    name = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN")
    publication_date = fields.Date()
    genre = fields.Many2one('openlib.genre',
        ondelete='set null', string="Genre", index=True)
    language = fields.Many2one('openlib.language',
        ondelete='set null', string="Language", index=True)

    author_id = fields.Many2many('res.partner', string="Author",
        ondelete='cascade', domain=[('author', '=', True)])
    publisher_id = fields.Many2one('res.partner', string="Publisher",
        ondelete='set null', domain=[('publisher', '=', True)])

    @api.constrains('author_id')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if len(r.author_id) == 0:
                raise exceptions.ValidationError("A book must have at least one author")


class BookGenre(models.Model):
    _name = 'openlib.genre'
    
    name = fields.Char(string="Genre", required=True)

class Language(models.Model):
    _name = 'openlib.language'

    name = fields.Char(string="Language", required=True)