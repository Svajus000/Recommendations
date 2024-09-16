import http.client

conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "df7e495db3msh4cc1ae136ae43e3p1fad3bjsnbafd385a5632",
    'x-rapidapi-host': "moviesdatabase.p.rapidapi.com"
}

film_title = "Shrek" 

conn.request("GET", f"/titles/search/akas/{film_title}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))