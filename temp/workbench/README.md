
option = {
    title : {
        text: '某站点用户访问来源',
        subtext: '纯属虚构',
        x:'center'
    },
    tooltip : {
        trigger: 'item',                     axis 竖线 item
        formatter: "{a} <br/>{b} : {c} ({d}%)"   提示的格式
    },
    legend: {                                图例
        orient: 'vertical',                  horizontal   横向  竖向
        left: 'left',                          左  中   右
        data: ['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']       数据项
    },
    series : [
        {
            name: '访问来源',                           数据名称
            type: 'pie',                                图表类型
            radius : '55%',                             半径
            center: ['50%', '60%'],                     中心位置 相对于div
            data:[                                      饼图数据
                {value:335, name:'直接访问'},
                {value:310, name:'邮件营销'},
                {value:234, name:'联盟广告'},
                {value:135, name:'视频广告'},
                {value:1548, name:'搜索引擎'}
            ],
            扇形的格式
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};