from django.shortcuts import render
import requests 

def index(request):
     r = requests.get('https://newsapi.org/v2/everything?q=apple&from=2023-02-24&to=2023-02-24&sortBy=popularity&apiKey=9d5388903e974cb49c82d2b150ce356d')
     res = r.json()
     data = res["articles"]
     author = []
     title = []
     source = []
     date = []
     url = []
     description = []
     for i in data:
        author.append(i['author'])
        title.append(i['title'])
        source.append(i['source']['name'])
        dates = i['publishedAt'].replace('T', ' ')
        dates = dates.replace ('Z','')
        date.append(dates)
        url.append(i['url'])
        description.append(i['description'])
     news = zip (author,title,description,date,url,source)
     return render (request, 'index.html', {'news':news})



