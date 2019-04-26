# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Shortcut(models.Model):
    _name = "workbench.shortcut"
    _rec_name = "action"
    _description = u"工作台-快捷动作"

    name = fields.Char(u'名称', help=u'在首页中的相应的文字显示内容')
    bench_id = fields.Many2one('workbench', string=u'工作台')
    sequence = fields.Integer(u'顺序')
    action = fields.Many2one('ir.actions.act_window', string=u'快捷动作')
    view_id = fields.Many2one('ir.ui.view', string=u'快捷动作视图')
    domain = fields.Char(u'页面的过滤', default='[]', help=u'字符串条件,用来过滤出您所选的视图中的数据!')
    context = fields.Char(u'动作的上下文', help=u'对应跳转视图传进去的参数!')
    is_active = fields.Boolean(u'是否可用', default=True)

    @api.onchange('action')
    def onchange_action(self):
        if self.action:
            return {
                'domain': {'view_id': [('model', '=', self.action.res_model), ('type', '=', 'tree')], }
            }
    @api.one
    def construction_action(self):
        """
        # jjjj    tree, form    ys.install    False    {}    354    安装单    current
        # False    tree, form    ys.city    False    {}    336    市    current
        :param action:
        :return:
        """
        return {'name': self.name, 'view_mode': self.action.view_mode, 'res_model': self.action.res_model,
                 'domain': self.action.domain, 'context': self.action.context, 'view_id': self.view_id.id,
                 'act_name': self.action.name, 'target': self.action.target}

