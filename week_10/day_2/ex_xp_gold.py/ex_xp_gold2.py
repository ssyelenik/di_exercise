import urllib.request,json,requests

def search_gifs(q):
    api_key="dc6zaTOxFJmzC"
    endpoint="http://api.giphy.com/v1/gifs/search"
    params={
        "q":q,
        "api_key":api_key
        }
    
    params={k:v for k,v in params.items() if v is not None}
    
    gifs=requests.get(endpoint,params=params)
    json_gifs=gifs.json()
    
    if len(json.dumps(json_gifs))>168:
        print("Here are the gifs for your query, {}:".format(q))
        print(json.dumps(json_gifs, sort_keys=True, indent=4))
    else:
        print("There were no gifs for query {}, but here's today's trending!\n".format(q))
        trending_gifs=requests.get("http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC&limit=5")
        json_trending_gifs=trending_gifs.json()
        print(json.dumps(json_trending_gifs,sort_keys=True, indent=4))
        


search_gifs("cheeseburgers")
