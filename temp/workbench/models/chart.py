# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Chart(models.Model):
    _name = "workbench.chart"
    _description = u"工作台-图表"

    name = fields.Char(u'名称', size=20)
    bench_id = fields.Many2one('workbench', string=u'所属工作台')
    type = fields.Selection([('echart3', u'echart3'), ('qweb', u'qweb模板')], string=u"图表类型")
    sequence = fields.Integer(u'顺序')
    is_active = fields.Boolean(u'是否可用', default=True)
    col = fields.Integer(u'列数', default=4)
    width = fields.Char(u'div宽度(px)', size=4)
    height = fields.Char(u'div高度(px)', size=4)

    model = fields.Char(u'业务对象', size=20)
    title = fields.Char(u'图表标题', size=10)
    subtitle = fields.Char(u'图表子标题', size=10)
    t_position = fields.Selection([('left', u'左'), ('center', u'中'), ('right', u'右')], string=u"图表标题显示位置")
    func = fields.Char(u'图表数据方法', help=u'返回图标需要的数据')

    t_name = fields.Char(u'qweb模板名称', size=30)
    t_model = fields.Char(u'业务对象', size=30)
    t_func = fields.Char(u'qweb模板数据方法', size=30)

    @api.constrains('col')
    def _check_col(self):
        if self.col > 12:
            raise Warning(u'列数不能大于12 ！')
