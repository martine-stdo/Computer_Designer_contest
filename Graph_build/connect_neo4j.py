import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher, Subgraph
import os

graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

def connect_neo4j_answer_to_question(folder_path):
    # 循环读取文件夹中的文件
    count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(file_path)
            # 读取数据
            df = pd.read_csv(file_path)
            # 创建问题和答案的节点集合
            a = df[['question', 'question_tag']]    # 从DataFrame中取出问题和问题标签
            b = df[['answer', 'answer_tag']]        # 从DataFrame中取出答案和答案标签
            b.columns = ['question', 'question_tag']  # 将答案的列名改为问题，标签也改为问题标签，便于拼接
            question = pd.concat([a, b])             # 将问题和答案合并为一个节点集合
            # 创建节点列表
            node_lis = []
            for i in question.values:
                node = Node(i[1], name=i[0])        # 创建每个问题或答案节点，其中节点标签为问题标签或答案标签，节点属性为问题或答案内容
                node_lis.append(node)               # 将节点添加到节点列表中
            # 创建包含所有节点的子图对象
            nodes = Subgraph(node_lis)
            # 将子图对象添加到Neo4j数据库中，从而创建这些节点
            graph.create(nodes)

            # 创建关系集合
            lis = []
            count = 0
            for i in df.values:
                count += 1
                c = graph.nodes.match(i[1], name=i[0]).first()
                d = graph.nodes.match(i[4], name=i[3]).first()
                rel_a = Relationship(c, i[2], d)
                lis.append(rel_a)

            # 导入关系
            nodes = Subgraph(relationships=lis)
            graph.create(nodes)
        count += 1
        print(count)
    return count

def connect_neo4j_model_to_answer(folder_path):
    count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(file_path)
            # 读取数据
            df = pd.read_csv(file_path)
            # 创建问题和答案的节点集合
            a = df[['question', 'question_tag']]  # 从DataFrame中取出问题和问题标签
            b = df[['model', 'model_tag']]  # 从DataFrame中取出答案和答案标签
            b.columns = ['question', 'question_tag']  # 将答案的列名改为问题，标签也改为问题标签，便于拼接
            question = pd.concat([a, b])  # 将问题和答案合并为一个节点集合
            # 创建节点列表
            node_lis = []
            for i in question.values:
                node = Node(i[1], name=i[0])  # 创建每个问题或答案节点，其中节点标签为问题标签或答案标签，节点属性为问题或答案内容
                node_lis.append(node)  # 将节点添加到节点列表中
            # 创建包含所有节点的子图对象
            nodes = Subgraph(node_lis)
            # 将子图对象添加到Neo4j数据库中，从而创建这些节点
            graph.create(nodes)

            # 创建关系集合
            lis = []
            count = 0
            for i in df.values:
                count += 1
                c = graph.nodes.match(i[1], name=i[0]).first()
                d = graph.nodes.match(i[4], name=i[3]).first()
                rel_a = Relationship(c, i[2], d)
                lis.append(rel_a)

            # 导入关系
            nodes = Subgraph(relationships=lis)
            graph.create(nodes)
        count += 1
        print(count)
    return count

count1 = connect_neo4j_model_to_answer('between_data\model')
count2 = connect_neo4j_answer_to_question('between_data\question_answer')
print(count1)
print(count2)
