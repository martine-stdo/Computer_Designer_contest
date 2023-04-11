var ec_right1 = echarts.init(document.getElementById('r1'), "dark");
var ec_right1_option = {
  title: {
    text: '累计确诊人数前八省份的治愈人数与死亡人数',
    subtext: 'Fake Data'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['治愈人数', '死亡人数']
  },
  toolbox: {
    show: true,
    feature: {
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  calculable: true,
  xAxis: [
    {
      type: 'category',
      data: []
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: '治愈人数',
      type: 'bar',
      data: []
      ,
    },
    {
      name: '死亡人数',
      type: 'bar',
      data: []
      ,
    }
  ]
};

ec_right1.setOption(ec_right1_option)
