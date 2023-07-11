from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    print('Client connected!')
    # 加入房间
    join_room(0)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected!')
    # 离开房间
    leave_room(0)

@socketio.on('message')
def handle_message(data):
    message = data['message']
    print('Message received: ' + message)
    # 广播消息给该房间的所有客户端
    emit('message', {'message': message}, room=0)
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=80,allow_unsafe_werkzeug=True)
