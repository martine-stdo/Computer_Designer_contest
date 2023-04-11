var f5_left = echarts.init(document.getElementById('f5l'), "dark");

var f5_left_option = {
  title: {
    text: '新增人数前30地级市(区)（除台湾外）',
    subtext: 'Fake Data',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [
    {
      name: '地级市',
      type: 'pie',
      radius: '65%',
      data: [],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};

f5_left.setOption(f5_left_option)