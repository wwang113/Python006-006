#使用 requests 库抓取豆瓣某电影的评论
#!/usr/bin/env python3


import requests
import re


def gain_yp(pg_num):
    comment_texts = []
    comment_stars = []
    comment_votess = []
    comment_times = []
    user_infos = []
        
    HEADERS = {
    	'Cookie': 'll="118172"; bid=8YOGihICZA0; __utmc=30149280; __utmz=30149280.1611628274.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1611628275.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=2e46ef0ce6e47502-22a3801ccec50032:T=1611628275:RT=1611628275:S=ALNI_MaqMRr2BTTd3akPMfk_nLhI_X7xDg; _vwo_uuid_v2=D5FB74756F8857E374F2F8CEB27390F14|bc043c93e55e50c62de2d2ce91ead374; __yadk_uid=J3oG6BlzupE2dDlpOXpp3Ce1hbeuzTvD; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1440396555.1611628274.1611628274.1611639807.2; __utmb=30149280.0.10.1611639807; __utma=223695111.1735551564.1611628275.1611628275.1611639807.2; __utmb=223695111.0.10.1611639807; _pk_id.100001.4cf6=c78eeb0c555142b3.1611628274.2.1611639848.1611629110.',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    
    for i in range(pg_num):
        url = f'https://movie.douban.com/subject/1295644/comments?start={i*20}&limit=20&status=P&sort=new_score'
        res = requests.get(url, headers=HEADERS, timeout=5)
        if res.status_code != 200:
            print(res.raise_for_status())

        # 评论内容
        comment_text = re.findall(re.compile('<span class=\"short\">(?s)(.+?)</span>'), res.text)
        # 评论时间
        comment_time = re.findall(r'<span class=\"comment-time \" title=\"(\d{4}-\d{2}-\d{2})', res.text)
        # 评论星数
        comment_star = re.findall(re.compile(r'(?:<span class=\"allstar\d{2} rating\" title=\"(\w+.?)\">'
                                                r'</span>)*(?:\s*?)<span class=\"comment-time \"'), res.text)
        # 评论用户昵称
        user_info = re.findall(re.compile(r'<a title=\"(.+?)\" href'), res.text)
        # 扩展一下信息
        comment_times.extend(comment_time)
        comment_texts.extend(comment_text)
        comment_stars.extend(comment_star)
        user_infos.extend(user_info)

    dy_info = {'names':user_infos, 'times':comment_times, 'stars':comment_stars, 'contents':comment_texts}
    
    return dy_info

if __name__ == '__main__':
    dy_content = str(gain_yp(5))
    with open('res.text', mode='w', encoding='utf-8') as f:
        f.write(dy_content)
    
        
