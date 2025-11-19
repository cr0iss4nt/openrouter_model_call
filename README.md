*or_request.py* contains a function called *model_request*, which accepts a prompt and returns the response from OpenRouter. The function is based on the HTTP request code written on the OpenRouter website.

In the current realization, you also need a .env file, which has to contain fields *OPENROUTER_API_KEY* (you can get it from your OpenRouter account) and *OPENROUTER_MODEL* (you can get the value from the dedicated model webpage).

The response is given in the JSON format. If you want just a text response and nothing more, use a realization similar to this:
```python
from or_request import call_model

raw_response = call_model("What's the meaning of life?")
response_json = raw_response.json()
final_response = response_json['choices'][0]['message']['content']
print(final_response)
```
