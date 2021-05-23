from odoo import models, fields, api
from datetime import timedelta

# 동물 타입
class zooanimaldata(models.Model):
    _name = 'zoo.feed_table'
    _description = 'feed data'

    animal_type_id = fields.Many2one('zoo.animal_type', string="Animal")
    food_type_id = fields.Many2one('zoo.food_type', string="Food Type")
    food_name_id = fields.Many2one('zoo.food_name', string="Food Name")
    animal_amount = fields.Float(string="Amount")
    # unit_id = fields.Many2one('')
    time = fields.Float('Duration in hours')

