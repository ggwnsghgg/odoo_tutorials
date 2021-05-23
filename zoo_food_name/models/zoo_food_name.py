from odoo import models, fields, api
from datetime import timedelta

# 동물 타입
class zoofoodname(models.Model):
    _name = 'zoo.food_name'
    _description = 'food data'

    name = fields.Char('Zoo Food Name')
    food_type_id = fields.Many2one('zoo.food_type', string="Food Type Id")

