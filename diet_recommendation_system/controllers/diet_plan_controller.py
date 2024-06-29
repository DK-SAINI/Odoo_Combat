# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import requests


class DietPlanController(http.Controller):
    @http.route("/user_diet_plan", auth="user", website=True)
    def user_diet_plan(self, **kw):
        
        user = request.env.user
        user_profile = request.env["user.profile"].sudo().search([('user_id', '=', user.id)])
        
        meals = [
            {
                "Time": "7:00 AM",
                "Recipe": "Quinoa and Black Bean Salad",
                "Ingredients": [
                    "Quinoa", "black beans", "bell pepper", "red onion", "corn",
                    "cilantro", "lime juice", "olive oil", "salt", "pepper"
                ],
                "Calories": 350,
                "Protein": 15,
                "Carbohydrates": 50,
                "Fats": 10
            },
            {
                "Time": "10:00 AM",
                "Recipe": "Chickpea and Vegetable Stir-fry",
                "Ingredients": [
                    "Chickpeas", "broccoli", "bell pepper", "carrots", "tofu",
                    "soy sauce", "garlic", "ginger", "sesame oil"
                ],
                "Calories": 400,
                "Protein": 20,
                "Carbohydrates": 45,
                "Fats": 12
            },
            {
               "Recipe":"Lentil and Vegetable Soup",
               "Time":"1:00 PM",
               "Ingredients":[
                  "Lentils, carrots, celery, onion, garlic, vegetable broth, tomatoes, cumin, coriander, bay leaf"
               ],
               "Calories":300,
               "Protein":18,
               "Carbohydrates":35,
               "Fats":8
            },
            {
               "Recipe":"Baked Tofu with Roasted Vegetables",
               "Time":"4:00 PM",
               "Ingredients":[
                  "Tofu, zucchini, bell pepper, eggplant, cherry tomatoes, olive oil, balsamic vinegar, basil, oregano"
               ],
               "Calories":380,
               "Protein":25,
               "Carbohydrates":30,
               "Fats":15
            }
        ]

        return request.render(
            "diet_recommendation_system.diet_plans",
            {
                "meals": meals
            },
        )