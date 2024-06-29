# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.Model):
    _name = "res.users"
    _inherit = ["res.users"]

    @api.model_create_multi
    def create(self, vals_list):
        user = super(Users, self).create(vals_list)
        if user:
            self.env["user.profile"].create({'user_id': user.id})
        return user
