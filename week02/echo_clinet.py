#不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。
#!/usr/bin/env python3
import socket

Host = '127.0.0.1'
Port = 9999

def client_sock():
    client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((Host, Port))
    while True:
        send_msg = input("input your file path:")
        if send_msg == "exit":
            break
        with open(send_msg, 'rb') ad f:
            data = f.read(1024)
            client.sendall(data)
        
        
        # data = client.recv(1024)
        # if not data:
        #     break
        # else:
        #     print(data.decode('utf-8'))
            
    client.close()
    
if __name__ == '__main__':
    client_sock()
        