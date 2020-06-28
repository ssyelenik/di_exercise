# Exercise 1:
# 1
import requests
import json
#data=requests.get("http://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=dc6zaTOxFJmzC")


##if data.status_code==200:
##    print(data.json())


def get_pics(q=None, rating=None):
    api_key="dc6zaTOxFJmzC"
    endpoint="http://api.giphy.com/v1/gifs/search"

    params={
        "q":q,
        "rating":rating,
        "api_key":api_key
        }
    
    params={k:v for k,v in params.items() if v is not None}
    
    response=requests.get(endpoint,params=params)

    json_response=response.json()

    #print(json_response)
    large_response=[]
    pic_widths=[]
    for i in range(0,10):
        for key,value in json_response["data"][i]["images"].items():
            try:
                if int(json_response["data"][i]["images"][key]["height"])>100:
                    #print(json_response["data"][i])
                    large_response.append(json_response["data"][i])
                    width=json_response["data"][i]["images"][key]["width"]
                    pic_widths.append(width)
                else:
                    print("PIC TOO SMALL")

            except:
                print("No HEIGHT param for pic")

    return large_response,pic_widths



large_response,pic_widths=get_pics(q="hilarious",rating="g")
print(large_response)
print(pic_widths)
