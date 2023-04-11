var ec_left1 = echarts.init(document.getElementById('l1'),"dark");

var ec_left1_option = {
	legend: {
        top: 'bottom'
    },
    title: {
        text: '新增病例数前十省份',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    toolbox: {
        show: true,
        feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
        }
    },
    series: [
        {
            name: '新增病例数前十省份',
            type: 'pie',
            radius: [20, 100],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
                borderRadius: 5
            },
            data: []
        }
    ]
};
ec_left1.setOption(ec_left1_option)