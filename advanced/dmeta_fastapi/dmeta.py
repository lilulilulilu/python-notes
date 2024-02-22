from sentence_transformers import SentenceTransformer

texts1 = ["胡子长得太快怎么办？", "在香港哪里买手表好"]
texts2 = ["胡子长得快怎么办？", "怎样使胡子不浓密！", "香港买手表哪里好", "在杭州手机到哪里买"]

model = SentenceTransformer('DMetaSoul/Dmeta-embedding')
embs1 = model.encode(texts1, normalize_embeddings=True)
embs2 = model.encode(texts2, normalize_embeddings=True)
print("embs1: ",embs1[0].tolist())

similarity = embs1 @ embs2.T
print(similarity)

for i in range(len(texts1)):
    scores = []
    for j in range(len(texts2)):
        scores.append([texts2[j], similarity[i][j]])
    scores = sorted(scores, key=lambda x:x[1], reverse=True)

    print(f"查询文本：{texts1[i]}")
    for text2, score in scores:
        print(f"相似文本：{text2}，打分：{score}")
    print()
