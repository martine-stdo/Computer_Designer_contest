var f5_right = echarts.init(document.getElementById('f5r'), "dark");
var f5_right_option = {
  title: {
    text: '各地级市疫情情况(除港澳台地区)'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {},
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'value',
    boundaryGap: [0, 0.01]
  },
  yAxis: {
    type: 'category',
    data: []
  },
  series: [
    {
      name: '死亡人数',
      type: 'bar',
      data: []
    },
    {
      name: '现存人数',
      type: 'bar',
      data: []
    },
  ]
};
f5_right.setOption(f5_right_option)