from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_game_data():
    url = 'https://gamedatabasestefan-skliarovv1.p.rapidapi.com/getGames'
    headers = {
        'X-RapidAPI-Key': '90c3b492c3msh8cc52b19c80277dp11dfa6jsn10f7a594733b',
        'X-RapidAPI-Host': 'GameDatabasestefan-skliarovV1.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    game_data = fetch_game_data()
    return render_template('index.html', game_data=game_data)

if __name__ == '__main__':
    app.run(debug=True)
