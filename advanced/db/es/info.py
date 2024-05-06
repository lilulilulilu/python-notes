from elasticsearch import Elasticsearch

# 连接到 Elasticsearch
es = Elasticsearch(
    'https://192.168.85.2:9020',
    basic_auth=('elastic', 'bd9cl4444444444444TC'),
    verify_certs=False  # 如果使用自签名证书，需要设置为 False
)

# 获取节点状态
nodes_stats = es.nodes.stats(metric='jvm')

def bytes_to_gb(bytes):
    """将字节转换为千兆字节（GB）"""
    return round(bytes / (1024**3), 2)

for node_id, node_info in nodes_stats['nodes'].items():
    print(f"节点 {node_id}")
    jvm_mem = node_info['jvm']['mem']
    print(f"已使用堆内存: 约 {bytes_to_gb(jvm_mem['heap_used_in_bytes'])} GB（{jvm_mem['heap_used_in_bytes']} 字节）")
    print(f"堆内存使用百分比: {jvm_mem['heap_used_percent']}%")

    # 年轻代内存
    young = jvm_mem['pools']['young']
    print(f"年轻代内存使用: 约 {bytes_to_gb(young['used_in_bytes'])} GB（{young['used_in_bytes']} 字节）")

    # 老年代内存
    old = jvm_mem['pools']['old']
    print(f"老年代内存使用: 约 {bytes_to_gb(old['used_in_bytes'])} GB（{old['used_in_bytes']} 字节）")

    # 幸存者区内存
    survivor = jvm_mem['pools']['survivor']
    print(f"幸存者区内存使用: 约 {bytes_to_gb(survivor['used_in_bytes'])} GB（{survivor['used_in_bytes']} 字节）")

    print()
    
    # 指定索引名称
    
index_name = "child_knowledge"  # 替换为您的索引名

# 获取索引信息
index_stats = es.indices.stats(index=index_name)
docs_count = index_stats['indices'][index_name]['total']['docs']['count']

print(f"Index: {index_name}")
print(f"Docs Count: {docs_count}")