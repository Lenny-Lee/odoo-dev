odoo.define('workbench.bench', function (require) {
'use strict';

var core = require('web.core');
var AbstractAction = require('web.AbstractAction');
var QWeb = core.qweb;
var Bench = AbstractAction.extend({
    init: function(parent, action) {
        this._super(parent, action);
        this.params = action.params;
    },
    willStart: function () {
        console.log('workbench')
        var self = this;
        self.datas=''
        // return $.when(this._super(),self.wb.call("client_start",[this.params['bench_id']]).done(function(result) {
        //         //     self.datas=result
        //         //     }));
        return this._rpc({
                model: 'workbench',
                method: 'client_start',
                args: [this.params['bench_id']],
                //context: this.given_context,
            })
            .then(function (result) {
                self.datas = result;
                console.log(result);
            });
    },
    events: {
    "click li": "click_action",
    },
//    快捷菜单点击跳转方法
    click_action: function (e) {
        var self=this;
        var action =self.datas['shortcuts']['actions'][$(e.currentTarget).data('index')]
        if (action){
            var view_modes=action['view_mode'].replace('tree','list').split(',');
            var views = [];
            for(var i=0;i<view_modes.length;i++){
                views.push([false, view_modes[i]])
            }
            self.do_action({
            type: 'ir.actions.act_window',
            res_model: action['res_model'],
            res_id: '',
            views: views,
            name:action['act_name'],
            target: action['target'],
            domain:action['domain'],
            context:action['context']});
             }
        },
//    按顺序创建图表方法
    render_echarts: function (option,i) {
        var self = this
        var div_id = 'c_div_id'+i
        $(QWeb.render('echart_t',{div_id:div_id,style:self.datas['charts'][i]['style']})).insertBefore(self.$el.find('#block_id'));
        echarts.init(self.$('#'+div_id)[0]).setOption(option);
        },
    start: function () {
        console.log('workbench start');
        var self = this;
        self.$el.append(QWeb.render("bench_t"));
        console.log(self.datas);
        if (self.datas['charts']){
            //    按顺序创建块
            for (var i in self.datas['charts']){
                if(self.datas['charts'][i]['type'] === 'echart3'){
                    self.render_echarts(self.datas['charts'][i]['options'],i)
                }else if(self.datas['charts'][i]['type'] === 'qweb'){
                    $(QWeb.render(self.datas['charts'][i]['t_name'],self.datas['charts'][i]['args'])).insertBefore(self.$el.find('#block_id'));
                }else{
                //显示快捷菜单 type === shortcut
                    $(QWeb.render('shortcut_t',{style:self.datas['shortcuts']['style'],shortcuts:self.datas['shortcuts']})).insertBefore(self.$el.find('#block_id'));
                }
            };
        }
        return self._super();
        }
        });
core.action_registry.add('workbench.bench_tag', Bench);
return Bench
});