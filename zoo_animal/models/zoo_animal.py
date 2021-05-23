from odoo import models, fields, api
from datetime import timedelta

# 동물 타입
class zooanimaldata(models.Model):
    _name = 'zoo.animal'
    _description = 'animal data'

    name = fields.Char('Zoo Name')
    animal_type_id = fields.Many2one('zoo.animal_type', string="Animal")
    animal_age = fields.Integer('Animal Age')
    animal_year = fields.Date('Animal Date')
    food_name_id = fields.Many2one('zoo.food_name', string="Animal Food")

