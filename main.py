import requests
import json
from flask import Flask
# import Flask

# text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text

# currencies = json.loads(text)

# for curr in currencies['Valute']:
#    print(curr)

# print(currencies)


app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(text)
    result = ''
    for curr in currencies['Valute']:
        result += str(curr) + '<br>'
    return result

if __name__ == "__main__":
    app.run()