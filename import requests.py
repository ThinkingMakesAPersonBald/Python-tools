import requests
from bs4 import BeautifulSoup

def get_definition(word):
    url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    definition = soup.find("span", {"class": "def"}).text.strip()
    return definition

word = "hello"
definition = get_definition(word)
print(f"The definition of '{word}' is: {definition}")