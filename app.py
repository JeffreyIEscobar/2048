from flask import Flask, render_template, request, jsonify
from game_logic import Numbers2048

app = Flask(__name__, static_url_path='/static')

game = Numbers2048()

@app.route('/')
def index():
    return render_template('index.html', board=game.board)

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    game.move(direction)
    game.add_tile()
    return jsonify({'board': game.board, 'score': game.score, 'game_over': game.is_game_over()})

if __name__ == '__main__':
    app.run(debug=True)
