import backoff
import openai

# タイムアウトとレート制限はリトライする
@backoff.on_exception(
    backoff.expo, (openai.error.Timeout, openai.error.RateLimitError), max_tries=10
)
def chat_completion_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


if __name__ == "__main__":
    try:
        response = chat_completion_with_backoff(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは役に立つアシスタントです。"},
                {"role": "user", "content": "2009年の第2回WBCで優勝した国はどこですか？"},
            ],
        )
        content = response.choices[0].message.content
        print(content)
    except openai.error.Timeout as e:
        # Handle timeout error, e.g. retry or log
        print(f"OpenAI API request timed out: {e}")
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
    except openai.error.APIConnectionError as e:
        # Handle connection error, e.g. check network or log
        print(f"Failed to connect to OpenAI API: {e}")
    except openai.error.InvalidRequestError as e:
        # Handle invalid request error, e.g. validate parameters or log
        print(f"OpenAI API request was invalid: {e}")
    except openai.error.AuthenticationError as e:
        # Handle authentication error, e.g. check credentials or log
        print(f"OpenAI API request was not authorized: {e}")
    except openai.error.PermissionError as e:
        # Handle permission error, e.g. check scope or log
        print(f"OpenAI API request was not permitted: {e}")
    except openai.error.RateLimitError as e:
        # Handle rate limit error, e.g. wait or log
        print(f"OpenAI API request exceeded rate limit: {e}")
    except Exception as e:
        print(f"unknown error: {e}")
