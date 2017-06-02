import os
import flask
import flask_socketio
import cardDeck

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

all_hands = []

@app.route('/')
def hello():
	cardDeck.getDeck()
	cardDeck.deal2player()
	return flask.render_template('index.html')
    
    
@socketio.on('connect')
def on_connect():
	flask_socketio.emit(
		'update', {
		'data': 'Working...'
		}
	)
	card = cardDeck.p1Hand[0].getImg()
	flask_socketio.emit(
		'hands', {
		'p1Hand': card
		}
	)
	

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
