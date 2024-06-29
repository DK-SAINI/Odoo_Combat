# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class UserProfileController(http.Controller):
    @http.route("/user_profile/update", auth="user", website=True)
    def update_user_profile(self, **kw):
        user = request.env.user
        user_profile = request.env["user.profile"].sudo().search([('user_id', '=', user.id)])
        return request.render(
            "diet_recommendation_system.user_profile_form",
            {
                "user": user_profile,
                "page_name": "user_profile",
            },
        )

    @http.route("/user_profile/save", auth="user", methods=["POST"], website=True)
    def save_user_profile(self, **post):
        user = request.env.user
        user_profile = request.env["user.profile"].sudo().search([('user_id', '=', user.id)])
        user_profile.write(
            {
                "age": post.get("age"),
                "gender": post.get("gender"),
                "weight": float(post.get("weight", 0.0)),
                "height": float(post.get("height", 0.0)),
                "dietary_preferences": post.get("dietary_preferences"),
                "allergies": post.get("allergies"),
                "health_goal": post.get("health_goals")
            }
        )
        return request.redirect("/my")
