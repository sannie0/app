import requests

def get_definition(word):
    lang = "en"
    url = f"https://{lang}.wiktionary.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "titles": word,
        "prop": "extracts",
        "exintro": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    pages = data["query"]["pages"]
    page_id = list(pages.keys())[0]
    if page_id == "-1":
        return False
    else:
        return True


word = "yf"
definition = get_definition(word)
print("Definition of", word + ":", definition)

