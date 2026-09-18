# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    profile_type = fields.Selection(
        selection=[
            ('patient', 'Paciente'),
            ('employee', 'Empleado'),
            ('doctor', 'Médico'),
            ('intern', 'Interno'),
        ],
        string='Tipo de Contacto',
        default='patient',
    )
