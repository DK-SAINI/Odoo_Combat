# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DietPlan(models.Model):
    _name = 'diet.plan'
    _description = 'Diet Plan'
    _rec_name = 'user_profile_id'

    user_profile_id = fields.Many2one('user.profile', string='User Profile', required=True)
    date = fields.Date(string='Date', required=True)
    meal_type = fields.Selection([
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ], string='Meal Type', required=True)
    meal_description = fields.Text(string='Meal Description')
    calories = fields.Float(string='Calories')
    protein = fields.Float(string='Protein (g)')
    fat = fields.Float(string='Fat (g)')
    carbs = fields.Float(string='Carbohydrates (g)')
    vitamins = fields.Text(string='Vitamins')
    minerals = fields.Text(string='Minerals')

    @api.model
    def generate_daily_plan(self, user_profile_id):
        # Logic to generate daily meal plan based on user profile
        pass

    @api.model
    def generate_weekly_plan(self, user_profile_id):
        # Logic to generate weekly meal plan based on user profile
        pass

    @api.model
    def generate_monthly_plan(self, user_profile_id):
        # Logic to generate monthly meal plan based on user profile
        pass
