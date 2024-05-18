from odoo import api, models, fields


class MaterialReq(models.Model):
    _name = "material.request"

    material_code = fields.Char(string="Material Code",required=True)
    material_name = fields.Char(string="Material Name",required=True)
    material_type_id = fields.Many2one('material.type', string='Material Type', required=True)
    material_price = fields.Float(string="Material Currency",required=True)
    partner_id = fields.Many2one('res.partner',string="Supplier Name",required=True)


class MaterialType(models.Model):
    _name = "material.type"

    name= fields.Char(string="Material Type Name")