from odoo import models, fields, api
from datetime import timedelta

# 동물 타입
class zoofooddata(models.Model):
    _name = 'zoo.food_type'
    _description = 'food data'

    name = fields.Char('Zoo Food')

