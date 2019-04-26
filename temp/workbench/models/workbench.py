# -*- coding: utf-8 -*-
import calendar
from datetime import date,datetime,timedelta
from math import floor

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class WorkBench(models.Model):
    _name = "workbench"
    _description = u"工作台"

    name = fields.Char(u'名称', default=u'工作台')
    shortcut_ids = fields.One2many('workbench.shortcut', 'bench_id', string=u'快捷动作', ondelete='cascade')
    shortcut_name = fields.Char(u'快捷动作显示名称', size=20)
    shortcut_seq = fields.Integer(u'快捷动作显示顺序')
    shortcut_col = fields.Integer(u'列数', default=4)
    chart_ids = fields.One2many('workbench.chart', 'bench_id', string=u'快捷动作', ondelete='cascade')

    @api.constrains('shortcut_col')
    def _check_shortcut_col(self):
        if self.shortcut_col > 12:
            raise Warning(u'列数不能大于12 ！')

    @api.model
    def get_shortcut(self, wb_id):
        """
        """
        shortcuts = self.env['workbench.shortcut'].search([('bench_id', '=', wb_id), ('is_active', '=', True)],
                                                          order='sequence desc')
        actions = []
        if len(shortcuts) > 0:
            for shortcut in shortcuts:
                actions.append(shortcut.construction_action()[0])
            return actions
        else:
            return False

    @api.model
    def get_chart(self, wb_id):
        """
        """
        charts = self.env['workbench.chart'].search([('bench_id', '=', wb_id), ('is_active', '=', True)],
                                                    order='sequence desc')
        cts = []
        c = {}
        if len(charts) > 0:
            for chart in charts:
                if chart.type == 'echart3':
                    if not hasattr(self.env[chart.model], chart.func):
                        raise ValidationError(u'%s 不存在：%s 属性' % (self.env[chart.model], chart.func))
                    else:
                        option = getattr(self.env[chart.model], chart.func)()
                        option['title'] = {'text': chart.title, 'subtext': chart.subtitle, 'x': chart.t_position}
                        option['tooltip'] = {'trigger': u'axis', 'show': True}
                        c['options'] = option
                        c['style'] = {'style': u'width: %spx; height: %spx' % (chart.width, chart.height),
                                      'col': u'quikecd col-md-%s'
                                             % chart.col}
                        c['type'] = chart.type
                        c['seq'] = chart.sequence
                        cts.append(c)
                        c = {}
                else:
                    if not hasattr(self.env[chart.t_model], chart.t_func):
                        raise ValidationError(u'%s 不存在：%s 属性' % (self.env[chart.t_model], chart.t_func))
                    else:
                        args = getattr(self.env[chart.t_model], chart.t_func)()
                        c['args'] = args
                        c['args']['style'] = {'style': u'width: %spx; height: %spx' % (chart.width, chart.height),
                                              'col': u'quikecd col-md-%s'
                                                     % chart.col}
                        c['t_name'] = chart.t_name
                        c['type'] = chart.type
                        c['seq'] = chart.sequence
                        cts.append(c)
                        c = {}
            return cts
        else:
            return False

    @api.model
    def client_start(self, wb_id):
        self = self.search([('id', '=', wb_id)])
        datas = {}
        shortcuts = self.get_shortcut(wb_id)
        if shortcuts:
            datas['shortcut'] = True
            datas['shortcuts'] = {'actions': shortcuts, 'shortcut_name': self.shortcut_name, 'style': {'col':
                                                                                                           u'quikecd col-md-%s' % self.shortcut_col}}
        else:
            datas['shortcut'] = False
        datas['charts'] = self.get_chart(wb_id)
        datas['charts'].append({'seq': self.shortcut_seq, 'type': 'shortcut'})
        datas['charts'] = sorted(datas['charts'], key=lambda item: item['seq'], reverse=True)
        return datas

    @api.model
    def gen_data(self):
        data = {}
        legend = {}
        xAxis = {}
        yAxis = {}
        series = {}
        legend['data'] = [u'销量1']
        xAxis['type'] = u'category'
        xAxis['data'] = [u"衬衫", u"羊毛衫", u"雪纺衫", u"裤子", u"高跟鞋", u"袜子"]
        yAxis['type'] = u'value'
        yAxis['data'] = []
        series['name'] = u'销量1'
        series['type'] = 'line'
        series['data'] = [5, 20, 40, 10, 10, 20]
        data['legend'] = legend
        data['xAxis'] = [xAxis]
        data['yAxis'] = [yAxis]
        data['series'] = [series]
        return data

    @api.model
    def gen_data1(self):
        data = {}
        legend = {}
        xAxis = {}
        yAxis = {}
        series = {}
        legend['data'] = [u'销量1']
        xAxis['type'] = u'category'
        xAxis['data'] = [u"衬衫", u"羊毛衫", u"雪纺衫", u"裤子", u"高跟鞋", u"袜子"]
        yAxis['type'] = u'value'
        yAxis['data'] = []
        series['name'] = u'销量1'
        series['type'] = 'bar'
        series['data'] = [5, 20, 40, 10, 10, 20]
        data['legend'] = legend
        data['xAxis'] = [xAxis]
        data['yAxis'] = [yAxis]
        data['series'] = [series]
        return data

    @api.model
    def q_test(self):
        return {'datas': [1, 2, 3, 4, 5, 6, 7, 8, 9]}
