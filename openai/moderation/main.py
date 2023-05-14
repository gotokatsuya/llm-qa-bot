import openai

if __name__ == "__main__":
    response = openai.Moderation.create(input="こんにちは")
    output = response["results"][0]
    print(output)
