import requests

def update_html(news,html_file,tag,y):
    for z in range(3):
        old_txt=tag+str(x)
        html_file=html_file.replace(old_txt,news["articles"][y][tag])
    return html_file

def get_news(country=None, category=None,sources=None,pageSize=None,q=None,page=None):


    api_key="b9de27fa168447f2ac7de99007e1f000"
    endpoint="http://newsapi.org/v2/top-headlines"

    params={
        'country':country,
        'category':category,
        'sources':sources,
        'pageSize':pageSize,
        'q':q,
        'page':page,
        'apiKey':api_key
        }

    params={k:v for k,v in params.items() if v is not None}

    

    #category="business"    

    r = requests.get(endpoint,params=params)
    return r.json()

news=get_news(country="us",category="general")

with open("index1.html") as file:

   html_file = file.read()

y=9
for x in range(3):
    print("*****",x,"******",news["articles"][y]["source"]["name"])
    old_txt="name"+str(x)
    html_file=html_file.replace(old_txt,news["articles"][y]["source"]["name"])
    print(news["articles"][y]["title"])
    html_file=update_html(news,html_file,"title",y)
    print(news["articles"][y]["author"])
    html_file=update_html(news,html_file,"author",y)
    print(news["articles"][y]["description"])
    html_file=update_html(news,html_file,"description",y)
    print(news["articles"][y]["urlToImage"])
    html_file=update_html(news,html_file,"urlToImage",y)
    y+=1


print(html_file)

with open('index2.html', 'w') as file:  

    file.write(html_file)
        
       

