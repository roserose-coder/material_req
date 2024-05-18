from odoo import http, _
from odoo.http import Controller, route, request
import json

class MaterialCont(Controller):


    @route('/all', auth='public',type="http")
    def my_test(self):

        materials = request.env["material.request"].sudo().search([])
        output="<ul>"
        for material in materials:
            output+="<li>"+material.material_name+"</li>"
        output+="</ul>"
        return output

