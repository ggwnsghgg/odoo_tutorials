from odoo import models, fields, api
from datetime import timedelta

# 동물 타입
class zooanimaldata(models.Model):
    _name = 'zoo.animal_type'
    _description = 'animal data'

    name = fields.Char('Zoo Animal')

