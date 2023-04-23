var f5_right = echarts.init(document.getElementById('f5r'), "dark");

var f5_right_option = {
  title: {
    text: '数据折线柱状图',
    subtext: 'Fake Data',
    left: 'left'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      crossStyle: {
        color: '#999'
      }
    }
  },
  toolbox: {
    feature: {
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  legend: {
    data: ['Amount', 'Precipitation', 'Proportion']
  },
  xAxis: [
    {
      type: 'category',
      data: ['交通',
      '婚姻',
      '债务',
      '房产',
      '劳动',
      '公司',
      '合同',
      '商标',
      '刑事',
      '民商',
      '民法',
      '行政'],
      axisPointer: {
        type: 'shadow'
      }
    }
  ],
  yAxis: [
    {
      type: 'value',
      name: 'Precipitation',
      min: 0,
      max: 1500,
      interval:75,
      axisLabel: {
        formatter: '{value} 条数'
      }
    },
    {
      type: 'value',
      name: 'Temperature',
      min: 0,
      max: 100,
      interval: 5,
      axisLabel: {
        formatter: '{value} %'
      }
    }
  ],
  series: [
    {
      name: 'Amount',
      type: 'bar',
      tooltip: {
        valueFormatter: function (value) {
          return value + ' 条数';
        }
      },
      data: [
        244, 1000,1000,990,577,1001,1047,39,998,537,572,9
      ]
    },
    {
      name: 'Proportion',
      type: 'line',
      yAxisIndex: 1,
      tooltip: {
        valueFormatter: function (value) {
          return value + ' %';
        }
      },
      data: [3.5, 12.48, 12.48, 12.35, 7.2, 12.49, 13.06, 0.49, 12.45, 6.7, 7.14, 0.11]
    }
  ]
};

f5_right.setOption(f5_right_option)