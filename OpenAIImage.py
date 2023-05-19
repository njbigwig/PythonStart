# API call to Open AI
# OPENAI_API_KEY is obtained from https://platform.openai.com/playground, click on account and select "View API Keys"
# Set as an environment variable under Windows Control Panel


import os
import openai # install via python -m pip install openai
import webbrowser

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)

print("OpenAI Response Data Type:")
print(type(response))

print("\nOpenAI Response:")
print(response)

print("\nOpenAI Image URL:")
print(response["data"][0]["url"])

print("\nLaunching browser to display image...\n")
webbrowser.open(response["data"][0]["url"])



