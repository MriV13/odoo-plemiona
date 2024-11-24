from odoo import api, fields, models, _


class WorldWorld(models.Model):
    _name = 'world.world'
    _description = 'World'
    
    name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    max_size_x = fields.Integer(default=100)
    max_size_y = fields.Integer(default=100)
    
    
    