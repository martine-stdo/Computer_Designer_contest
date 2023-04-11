var ec_left2 = echarts.init(document.getElementById('l2'), "dark");
var ec_left2_option = {
  title: {
    text: '每日病例情况'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['新增无症状感染者', '新增本土病例', '新增死亡', '新增痊愈']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: []
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '新增无症状感染者',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: '新增本土病例',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: '新增死亡',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: '新增痊愈',
      type: 'line',
      stack: 'Total',
      data: []
    }
  ]
};
ec_left2.setOption(ec_left2_option)