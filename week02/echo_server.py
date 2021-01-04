#不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。
#!/user/bin/env python3

import socket

Host = '127.0.0.1'
Port = 9999

def server_echo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((Host, Port))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(f'connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            with open('/data/filename', 'a') as f:
                f.write(data)
#            conn.sendall(data)
        conn.close()
    s.close()
    

if __name__ == '__main__':
    server_echo()

