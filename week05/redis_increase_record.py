#!/usr/bin/env python3

import redis

client = redis.Redis(host='127.0.0.1', password='')


def counter(video_id: int):
    
    if client.exists(str(video_id)):
        pass
    else:
        client.set(str(video_id), 0)
    
    count_number = client.incr(str(video_id))

    return count_number
    
if __name__ == '__main__':
    #vid = input("请输入video的id(数字):")
    list = [1000, 1001, 1002, 1003, 1004, 1005]
    for i in list:
        vl = counter(i)
        print(f'{i}返回值为: {vl}')