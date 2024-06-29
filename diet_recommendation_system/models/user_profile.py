# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UserProfile(models.Model):
    _name = "user.profile"
    _description = "User Profile"
    _rec_name = 'user_id'

    user_id = fields.Many2one("res.users", string="User", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    dietary_preferences = fields.Text(string="Dietary Preferences")
    allergies = fields.Text(string="Allergies")
    health_goal = fields.Selection([("weight_loss", " Weight Loss"), ("weight_gain", "Weight Gain")], string="Health Goal")
    