import openai
import numpy as np

def get_embedding(text):
    # 埋め込み時に改行が存在すると想定どおりの結果が得られないことがあるらしいので、スペースに変換する
    text = text.replace("\n", " ")
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
      )
    return response['data'][0]['embedding']

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def euclidean_distance(a, b):
  return np.linalg.norm(np.array(a) - np.array(b))

if __name__ == "__main__":
    target = "おはようございます"
    target_embedding = get_embedding(target)
    similarities = []
    # このデータの中からターゲットに近いものを検索する
    for text in ["おはよう", "こんにちは", "こんばんは", "おやすみ"]:
      embedding = get_embedding(text)
      # TODO ユークリッド距離に変更してみましょう
      # similarity = euclidean_distance(target_embedding, embedding)
      similarity = cosine_similarity(target_embedding, embedding)
      similarities.append({"text": text, "similarity": similarity})
    # TODO ユークリッド距離を使う場合は昇順
    # similarities.sort(key=lambda x: x['similarity'], reverse=False)
    similarities.sort(key=lambda x: x['similarity'], reverse=True)
    print(similarities[0]["text"])
