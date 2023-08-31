from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit, join_room, leave_room
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    file = open('file.txt', "r", encoding="utf-8")
    content = file.read()
    content_html = content.replace('\n', '<br><br>')
    return render_template('index.html',content = content_html)


@socketio.on('connect')
def handle_connect():
    print(request.sid)
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
    # 定义 CSV 文件路径和文件名
    # 定义文本文件路径和文件名
    txt_file_path = 'file.txt'
    message = time.strftime("%m/%d %H:%M ", time.localtime())+message
    # 写入数据到文本文件
    file = open(txt_file_path, "a", encoding="utf-8")
    file.write(message + '\n')
    # 广播消息给该房间的所有客户端
    emit('message', {'message':message}, room=0)
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=80,allow_unsafe_werkzeug=True)
