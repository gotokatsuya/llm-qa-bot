import openai

if __name__ == "__main__":
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "あなたは役に立つアシスタントです。"},
          {"role": "user", "content": "2009年の第2回WBCで優勝した国はどこですか？"},
          {"role": "assistant", "content": "2009年の第2回WBCで優勝したのは、日本です。"},
          {"role": "user", "content": "最も活躍した選手は誰ですか？"}
        ]
    )
    content = response.choices[0].message.content
    print(content)
