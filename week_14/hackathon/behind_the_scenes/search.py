import requests

def make_plans(param):

    url="https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    param=param
    url_end="&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyDpHrh1whEMZ0zOr5ZedF-b5mfjcRX8xSI"

    ###https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=national%20park%20montana&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyDpHrh1whEMZ0zOr5ZedF-b5mfjcRX8xSI

    endpoint=url+param+url_end
    response=requests.get(endpoint)
    x=response.json()
    return x