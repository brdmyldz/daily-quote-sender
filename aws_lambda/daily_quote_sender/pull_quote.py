import requests

# List of tags can be found at https://api.quotable.io/tags
# Change tags as you like
TAGS = ["happiness", "inspirational", "life", "love", "motivational", "power-quotes", "success", "time", "truth", "wisdom"]
URL = "https://api.quotable.io/random"
TAGS_STRING = "|".join(TAGS)
PARAMS = {"tags": TAGS_STRING}


def pull_quote():
    request = requests.get(url = URL, params = PARAMS)
    data = request.json()
    quote = data["content"]
    author = data["author"]
    message = "'" + quote + "' - " + author
    return message