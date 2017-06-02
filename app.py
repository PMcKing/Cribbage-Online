import os
import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')
    
@socketio.on('connect')
def on_connect():
    print 'Someone connected!'

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
