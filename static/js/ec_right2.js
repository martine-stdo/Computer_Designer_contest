var ec_right2 = echarts.init(document.getElementById('r2'), "dark");
var ec_right2_option = {
  title: {
    text: '病例总情况'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['现有无症状感染者', '现有本土病例', '累积死亡', '累计痊愈']
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
      name: '现有无症状感染者',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: '现有本土病例',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: '累积死亡',
      type: 'line',
      stack: 'Total',
      data: []
    },
    {
      name: '累计痊愈',
      type: 'line',
      stack: 'Total',
      data: []
    }
  ]
};
ec_right2.setOption(ec_right2_option)