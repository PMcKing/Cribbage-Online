import os
import flask
import flask_socketio
import cardDeck

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
	cardDeck.getDeck()
	return flask.render_template('index.html')
    #getting desk
    
@socketio.on('connect')
def on_connect():
	flask_socketio.emit('update', {
		'data': 'Working...'
	})
	

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
