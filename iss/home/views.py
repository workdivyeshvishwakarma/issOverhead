import json
from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.content
    processedData = json.loads(data)
    isslat = processedData["iss_position"]["latitude"]
    isslon = processedData["iss_position"]["longitude"]
    mylat = '19.08632'
    mylon = '72.89661'
    isIssOverMyHead = (isslat == mylat and isslon == mylon)
    context = {
        "data": {"isslat":isslat, "isslon": isslon}, 
        "isIssOverMyHead": isIssOverMyHead,
        "myData": {"mylat":mylat, "mylon": mylon}
    }
    return render(request, 'home/index.html', context)