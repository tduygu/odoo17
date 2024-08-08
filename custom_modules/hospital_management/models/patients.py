from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    ref = fields.Char(string='Ref')
    name = fields.Char(string='Name')
    dob = fields.Date(string='Date of birth')
    # age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    image = fields.Image(string='Image')
    father_name = fields.Char(string='Father Name')
    marital_status = fields.Selection([('single', 'Single'), ('married', 'Married')])
    # phone
    # email
    active = fields.Boolean(string='Active', default=True)


