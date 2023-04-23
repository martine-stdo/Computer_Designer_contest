var f5_left = echarts.init(document.getElementById('f5l'), "dark");

var f5_left_option = {
  title: {
    text: '各模块提问占比',
    subtext: '',
    left: '20px',
    top: '70px'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b}: {c} ({d}%)'
  },
  legend: {
    data: [
      '交通',
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
      '行政'
    ]
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      selectedMode: 'single',
      radius: [0, '30%'],
      label: {
        position: 'inner',
        fontSize: 14
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 3234, name: '个人' },
        { value: 2664, name: '组织' },
        { value: 2116, name: '社会', selected: true }
      ]
    },
    {
      name: 'Access From',
      type: 'pie',
      radius: ['45%', '60%'],
      labelLine: {
        length: 30
      },
      label: {
        formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
        backgroundColor: '#F6F8FC',
        borderColor: '#8C8D8E',
        borderWidth: 1,
        borderRadius: 4,
        rich: {
          a: {
            color: '#6E7079',
            lineHeight: 22,
            align: 'center'
          },
          hr: {
            borderColor: '#8C8D8E',
            width: '100%',
            borderWidth: 1,
            height: 0
          },
          b: {
            color: '#4C5058',
            fontSize: 14,
            fontWeight: 'bold',
            lineHeight: 33
          },
          per: {
            color: '#fff',
            backgroundColor: '#4C5058',
            padding: [3, 4],
            borderRadius: 4
          }
        }
      },
      data: [
        { value: 244, name: '交通' },
        { value: 1000, name: '婚姻' },
        { value: 1000, name: '债务' },
        { value: 990, name: '房产' },
        { value: 577, name: '劳动' },
        { value: 1001, name: '公司' },
        { value: 1047, name: '合同' },
        { value: 39, name: '商标' },
        { value: 998, name: '刑事' },
        { value: 537, name: '民商' },
        { value: 572, name: '民法' },
        { value: 9, name: '行政' }
      ]
    }
  ]
};

f5_left.setOption(f5_left_option)