# -*- coding: utf-8 -*-
import os
from odoo import http
from flask import Flask, render_template
import logging

logging.basicConfig(level=logging.INFO)
BASE_DIR =os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=os.path.join(BASE_DIR, 'static/dist'), template_folder=os.path.join(BASE_DIR, 'static'))


# BASE_DIR =  os.path.dirname(os.path.abspath(__file__))

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    # @app.route("/academy/academy")
    def index(self, **kw):
				# filename = os.path.join(BASE_DIR, 'form.html')
        return render_template('index.html')
        # return "hello world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })