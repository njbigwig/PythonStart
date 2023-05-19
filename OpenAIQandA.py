# API call to Open AI
# OPENAI_API_KEY is obtained from https://platform.openai.com/playground, click on account and select "View API Keys"
# Set as an environment variable under Windows Control Panel
#
# sample response:
# {
#  "choices": [
#    {
#      "finish_reason": "stop",
#      "index": 0,
#      "logprobs": null,
#      "text": "\nMacbeth is a story about a brave warrior named Macbeth. He is a brave and loyal soldier who is very proud of his accomplishments. One day he meets three witches who make a prophecy that he will become the King of Scotland. Macbeth is tempted by his ambition and decides to take matters into his own hands by killing the current king and taking the throne for himself. He does this with the help of his wife, Lady Macbeth. After becoming king, Macbeth begins to have a guilty conscience and is haunted by nightmares. Eventually, Macbeth is defeated in battle and killed by the rightful king of Scotland."
#    }
#  ],
#  "created": 1684519595,
#  "id": "cmpl-7HympJNahOb4y4hz7VI0Rv7PI4Lz8",
#  "model": "text-davinci-003",
#  "object": "text_completion",
#  "usage": {
#    "completion_tokens": 131,
#    "prompt_tokens": 15,
#    "total_tokens": 146
#  }
# }

import os
import openai # install via python -m pip install openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
 model="text-davinci-003",
  prompt="summarize shakespeare's Macbeth for a second grader\n",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print("OpenAI Response Data Type:")
print(type(response))

print("\nOpenAI Response:")
print(response)

print("\nOpenAI Answer:")
print(response["choices"][0]["text"])