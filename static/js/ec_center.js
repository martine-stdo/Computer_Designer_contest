var ec_center = echarts.init(document.getElementById('c2'), "dark");
var mydata = []
var ec_center_option = {
    title: {
        text: '疫情分布地图',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标

    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 0,end: 0 },
            { start: 1,end: 9 },
            { start: 10,end: 99 },
            { start: 100, end: 499 },
			{ start: 500, end: 1999 },
            { start: 2000, end: 30000 },
        ],
        color: ['#8A3310','#C64918', '#B55B25', '#F2AD92','#F9DCD1','white']
    },

    //配置属性
    series: [{
        name: '现存病例数',
        type: 'map',
        mapType: 'china',
        roam: true, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#009fe8', //区域边框颜色
                areaColor: "#f8f8ff", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data:[] //mydata //数据
    }]
};
ec_center.setOption(ec_center_option)