import requests
import json

# credenciales de la api
app_id = "cabc512f"
app_key = "3b63add2d492321f11b2cc2d2acabe58"

# configuraciones de la request

language = "es"
word_id = "amor"
fields = "definitions"
strictMatch = "false"

url = (
    "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
    + language
    + "/"
    + word_id.lower()
    + "?fields="
    + fields
    + "&strictMatch="
    + strictMatch
)

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)

response = r.json()
response = response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]

# funcion que trae todas las definiciones de la palabra
for definicion in range(0, len(response)):
    print(response[definicion]["definitions"][0] + "\n")
