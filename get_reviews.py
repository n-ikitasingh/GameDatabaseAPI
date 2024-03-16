import http.client

conn = http.client.HTTPSConnection("gamedatabasestefan-skliarovv1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "90c3b492c3msh8cc52b19c80277dp11dfa6jsn10f7a594733b",
    'X-RapidAPI-Host': "GameDatabasestefan-skliarovV1.p.rapidapi.com"
}

conn.request("POST", "/getReviews", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))