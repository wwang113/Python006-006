#!/usr/bin/env python3

'''
在使用短信群发业务时，公司的短信接口限制接收短信的手机号，每分钟最多发送五次，请基于 Python 和 redis 实现如下的短信发送接口：
已知有如下函数：

复制代码
def sendsms(telephone_number: int, content: string, key=None)：
    # 短信发送逻辑, 作业中可以使用 print 来代替
    pass
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后
    pass
    print("发送成功")
'''
import redis

client = redis.Redis(host='127.0.0.1', password='')

#def sendsms(telephone_number: int, content: string, key=None):
def send_times(telephone_number: int):
    if len(str(telephone_number)) != 11:
        print('手机号码不正确，请重新输入！')
        exit(1)
        
    num_id = client.exists(str(telephone_number))
    if not num_id:
        client.set(str(telephone_number), 1, ex=60)
        times = 1
    else:
        client.incr(str(telephone_number))
        times = int(client.get(str(telephone_number)).decode())
        #print(times)
    if times > 5:
        print('1分钟内发送次数超过5次，请等待一分钟再查询.')
        exit(1)
        
def sendsms(telephone_number: int, content):
    con_len = len(content)
    limit_len = 70
    if con_len > limit_len:
        start = 0
        end = limit_len
        while con_len > 0:
            con_len = len(content[end:-1])
            cont = content[start:end]
            print(f'发送消息: {cont}')
            start = end
            end = start + limit_len
    else:
        print(f'发送消息: {content}')
            
if __name__ == '__main__':
    content = 'hello'
    phonenum = input('请输入手机号码:')
    pnum = int(phonenum)
    send_times(pnum)
    sendsms(pnum, content)    
    
    
    
            
    
        
        
    
    
        
