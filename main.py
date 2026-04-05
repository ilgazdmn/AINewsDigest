import requests
from langchain.chat_models import init_chat_model
from send_email import send_email
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
api_key=os.getenv('NEWS_API_KEY')

topic='intelligenza artificiale'
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'from=2026-03-12&'
       'sortBy=publishedAt&'
       'apiKey='+api_key+"&"+
       'language=en')
#make request
request = requests.get(url)

#get a dictionary with data
content = request.json()
articles = content['articles']
print(articles)

#AI Summarizing the news

model = init_chat_model(
    model='gemini-3-flash-preview',
    model_provider='google-genai',
    api_key=GOOGLE_API_KEY
)
prompt=f"""You're a news analizer
Write a short paragraph analyzing those news
and tell me how they effect the stock
Summarize the following article
Here are the news articles:{articles}
"""
response = model.invoke(prompt)
response_str=response.content[0]["text"]


body=("Subject:News Summmary\n\n" +
      response_str +
      "\n\n")
print(body)
body=body.encode('utf-8')
send_email(message=body)