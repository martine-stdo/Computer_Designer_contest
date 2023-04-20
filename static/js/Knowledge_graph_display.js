import neo4j from 'neo4j-driver';

// 创建Neo4j驱动程序实例
const driver = neo4j.driver('bolt://localhost:7687', neo4j.auth.basic('neo4j', '12345678'));

// 获取图谱数据
async function getGraphData() {
    const session = driver.session();
    try {
        const result = await session.run('MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 50');
        return result.records;
    } finally {
        session.close();
    }
}

// 将图谱数据转换为vis.js兼容的格式
function prepareDataForVis(records) {
    const nodes = [];
    const edges = [];

    records.forEach(record => {
        const n = record.get('n');
        const m = record.get('m');
        const r = record.get('r');

        nodes.push({ id: n.identity.toString(), label: n.properties.name });
        nodes.push({ id: m.identity.toString(), label: m.properties.name });

        edges.push({ from: n.identity.toString(), to: m.identity.toString(), label: r.type });
    });

    return { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
}

// 渲染关系图谱
async function renderGraph() {
    const graphContainer = document.getElementById('graph');
    const graphData = await getGraphData();
    const { nodes, edges } = prepareDataForVis(graphData);

    const options = {
        nodes: {
            shape: 'dot',
            size: 20,
            font: {
                size: 14,
                color: '#000000'
            },
            borderWidth: 2
        },
        edges: {
            width: 2
        }
    };

    const network = new vis.Network(graphContainer, { nodes, edges }, options);
}

// 在页面加载时调用renderGraph
renderGraph();
