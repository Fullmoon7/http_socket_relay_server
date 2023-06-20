from flask import Flask, request, jsonify, render_template
import socket
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')
client_socket = socket.socket
hostname = '127.0.0.1'
port = 14444


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


@app.route('/SubmitRequest', methods=['POST'])
def submit_request():
    socket_init()
    print("submit_request")
    data = request.get_json()
    mode = data['chargeMode']
    amount = data['requestCharge']
    time = data['createTime']
    name = data['usrname']
    message = ['__SubmitRequest', {
        'chargeMode': mode,
        'requestCharge': amount,
        'createTime': time,
    }, name]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/ShowDetailedBill', methods=['POST'])
def show_detailed_bill():
    socket_init()
    print("show_detailed_bill")
    data = request.get_json()
    name = data['name']
    message = ['__ShowDetailedBill', name]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/GetRIinfo', methods=['POST'])
def get_ri_info():
    socket_init()
    print("getRIinfo")
    data = request.get_json()
    name = data['name']
    message = ['__GetRIinfo', name]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/StopCharge', methods=['POST'])
def stop_charge():
    socket_init()
    print("stop charge")
    data = request.get_json()
    name = data['name']
    message = ['__StopCharge', name]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Changemode', methods=['POST'])
def change_mode():
    socket_init()
    print("change mode")
    data = request.get_json()
    name = data['name']
    message = ['__Changemode', name]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Changerequest', methods=['POST'])
def change_request():
    socket_init()
    print("change request")
    data = request.get_json()
    name = data['name']
    amount = data['amount']
    message = ['__Changerequest', name, amount]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Stopuppile', methods=['POST'])
def stop_up_pile():
    socket_init()
    print("stop up pile")
    data = request.get_json()
    pile_no = data['pile_no']
    message = ['__Stopuppile', pile_no]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/GetPilen', methods=['POST'])
def get_pilen():
    socket_init()
    print("get pilen")
    message = ['__GetPilen']
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Showpile', methods=['POST'])
def show_pile():
    socket_init()
    print("show pile")
    data = request.get_json()
    pile_no = data['pile_no']
    message = ['__Showpile', pile_no]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Showcars', methods=['POST'])
def show_cars():
    socket_init()
    print("show cars")
    data = request.get_json()
    pile_no = data['pile_no']
    message = ['__Showcars', pile_no]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Getreportform', methods=['POST'])
def get_report_form():
    socket_init()
    print("get report form")
    data = request.get_json()
    pile_no = data['pile_no']
    message = ['__Getreportform', pile_no]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/Getwaitinginfo', methods=['POST'])
def get_waiting_info():
    socket_init()
    print("get waiting info")
    message = ['__Getwaitinginfo']
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/GetSysTime', methods=['POST'])
def get_sys_time():
    socket_init()
    print("get system time")
    message = ['__GetSysTime']
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/BreakDownPile', methods=['POST'])
def break_down_pile():
    socket_init()
    print("break down pile")
    data = request.get_json()
    pile_no = data['pile_no']
    action = data['action']
    message = ['__PileBreakDown', pile_no, action]
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/ResetSysTime', methods=['POST'])
def reset_sys_time():
    socket_init()
    print("reset system time")
    message = ['__ResetTime']
    send_message(json.dumps(message))
    message = recv_message()
    close_socket()
    return message


@app.route('/', methods=['GET'])
def homepage():
    print("hello")


def socket_init():
    global client_socket
    global hostname
    global port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hostname, port))
    print("connected")


def close_socket():
    global client_socket
    print("socket closed")
    client_socket.shutdown(socket.SHUT_RDWR)
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
    app.run(debug=True, port=8000, host='0.0.0.0')
