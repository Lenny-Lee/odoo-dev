# -*- coding: utf-8 -*-
import json
import logging
from datetime import datetime, timedelta
from odoo import http

_logger = logging.getLogger(__name__)


class FilterBar(http.Controller):
    @http.route('/dm_wx_filterbar', type='http', auth="public", methods=["POST"], csrf=False, website=True)
    def dm_wx_filterbar(self, d_pram, j_pram, c_pram):
        d_val = int(d_pram)
        j_val = int(j_pram)
        c_val = int(c_pram)
        car_data, reserve_data, profit_data = http.request.env['workbench'].wx_sum_datas(d_val, j_val, c_val)
        return json.JSONEncoder().encode({'car_data': car_data, 'reserve_data': reserve_data, 'profit_data': profit_data})

    @http.route('/dm_ck_filterbar', type='http', auth="public", methods=["POST"], csrf=False, website=True)
    def dm_ck_filterbar(self, d_pram, c_pram):
        d_val = int(d_pram)
        c_val = int(c_pram)
        out_data, in_data = http.request.env['workbench'].ck_sum_datas(d_val, c_val)
        return json.JSONEncoder().encode({'out_data': out_data, 'in_data': in_data})

    @http.route('/dm_xm_filterbar', type='http', auth="public", methods=["POST"], csrf=False, website=True)
    def dm_xm_filterbar(self, d_pram, j_pram, c_pram):
        d_val = int(d_pram)
        j_val = int(j_pram)
        c_val = int(c_pram)
        car_data, reserve_data, profit_data = http.request.env['workbench'].xm_sum_datas(d_val, j_val, c_val)
        return json.JSONEncoder().encode({'car_data': car_data, 'reserve_data': reserve_data, 'profit_data': profit_data})

