from flask import Flask, request, jsonify, render_template
import socket
import json
app = Flask(__name__)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


@app.route('/Register', methods=['POST'])
def register():
    socket_init()
    print("registering")
    data = request.get_json()
    name = data['name']
    password = data['password']
    account_type = data['type']
    message = ['__Register', name, password, account_type]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


# User login endpoint
@app.route('/Login', methods=['POST'])
def login():
    socket_init()
    print("logining")
    data = request.get_json()
    name = data['name']
    password = data['password']
    account_type = data['type']
    message = ['__Login', name, password, account_type]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/', methods=['POST'])
def homepage():
    print("hello")


def socket_init():
    global client_socket
    client_socket.connect(('127.0.0.1', 8080))
    print("connected")


def close_socket():
    global client_socket
    print("socket closed")
    client_socket.close()


def send_message(message):
    global client_socket
    print("send message = " + message)
    client_socket.send(message.encode('ascii'))


def recv_message():
    global client_socket
    message = client_socket.recv(1024)
    print("received message = " + message.decode('ascii'))
    return message.decode('ascii')


if __name__ == '__main__':
    socket_init()
    print("hello")
    app.run(debug=True, port=8000)
