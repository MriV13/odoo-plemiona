from odoo import api, fields, models, _


class VillageVillage(models.Model):
    _name = 'village.village'
    _description = 'Village'
    
    name = fields.Char()
    
    
    
    