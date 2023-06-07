# tcp client that sends messages to the microcontroller
# the messages have a format that the program must respect


import socket
import datetime

TCP_IP = '192.168.88.188'
TCP_PORT = 7
BUFFER_SIZE = 1024

LOCAL_IP_ADDRESS = '192.168.88.187'.split('.')

START_BYTE = '{'
END_BYTE   = '}'
TYPE_BYTE_A  = 'a'
TYPE_BYTE_B  = 'b'
END_PAYLOAD_BYTE = '#'

#----------------------------------NEW USER----------------------------#

def send_new_user_message_to_mc(username):
    mc_message = build_new_user_message(username)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(mc_message)


def build_new_user_message(username):
    return bytearray(START_BYTE + TYPE_BYTE_A, 'utf-8')  + get_current_date_as_bytearray() + bytearray(username + END_PAYLOAD_BYTE + END_BYTE, 'utf-8')


def get_current_date_as_bytearray():
    date = datetime.datetime.now()
    date_as_list = []
    date_as_list.append(date.year-2000)
    date_as_list.append(date.month)
    date_as_list.append(date.day)
    date_as_list.append(date.hour)
    date_as_list.append(date.minute)
    date_as_list.append(date.second)
    return bytearray(date_as_list)


#----------------------------------GET DATES---------------------------#

def get_dates_from_user(username):
    mc_message = build_get_dates_from_user_message(username)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(mc_message)

    data = s.recv(BUFFER_SIZE)
    s.close()
    print("received data:", data)

def build_get_dates_from_user_message(username):
    return bytearray(START_BYTE + TYPE_BYTE_B, 'utf-8') + get_local_ip_as_bytearray() + bytearray(username + END_PAYLOAD_BYTE + END_BYTE, 'utf-8')

def get_local_ip_as_bytearray():
    ip_as_list = []
    for ip_bit in LOCAL_IP_ADDRESS:
        ip_as_list.append(int(ip_bit))
    ip_as_list.append(TCP_PORT)
    return bytearray(ip_as_list)
    

#send_new_user_message_to_mc("alejandro")
#send_new_user_message_to_mc("pepe")
#send_new_user_message_to_mc("pepe")
#send_new_user_message_to_mc("pepe")
#send_new_user_message_to_mc("pedro")
#send_new_user_message_to_mc("antonio")

#get_dates_from_user("pepe")

