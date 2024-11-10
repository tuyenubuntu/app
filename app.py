from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Khởi tạo Flask app và Flask-SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Định nghĩa route để render giao diện chat
@app.route('/')
def index():
    return render_template('template.html')

# Lắng nghe sự kiện 'message' từ client và gửi lại tin nhắn
@socketio.on('message')
def handle_message(msg):
    print('Nhận được tin nhắn: ' + msg)
    send(msg, broadcast=True)  # Gửi tin nhắn cho tất cả các client đang kết nối

# Chạy app
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=5000, debug=True)
