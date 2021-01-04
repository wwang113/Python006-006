#使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件
#/usr/bin/env python3
import requests
import json
import jsonlines

Cookie = ' KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1609737782|1609737750; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1609737755; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1609726556,1609726575,1609726709,1609727037; JOID=Vl8TA0vthw8f_jGDeumwmoDA7Qhpo_E_bIMB4y6q92N0jkPNGdQI-0T5M4R8Tgs3Hz8qdGiWePaztZVIuFekkL0=; SESSIONID=Mw6sy3aRCsmmpvMbhmWOGKjv6dxydJanqkRuY2e9K4o; osd=UVEVBU3qiQkZ-DaNfO-2nY7G6w5urfc5aoQP5Sis8G1yiEXKF9IO_UP3NYJ6SQUxGTktem6QfvG9s5NOv1milrs=; tst=r; tshl=; q_c1=564a3993c743437f98fcc60114964f8b|1609674890000|1519267474000; z_c0="2|1:0|10:1609674809|4:z_c0|92:Mi4xQk5LMUFnQUFBQUFBWUtCRVNSYUpEU1lBQUFCZ0FsVk5PZjdlWUFBYWpNbGZ1NUZHeHowYnNqMHBSUGpQZmtmbnJB|fe0836fb7f9f1d4759f86f5987d57c69158642969f0498673dbd00347a07a26b"; capsion_ticket="2|1:0|10:1609674774|14:capsion_ticket|44:OWM4MzkxNDc0OTFlNGRmM2E4YjM3NTVlYjFiY2MzODQ=|87bbeea751ec2f29e314d083f8ac7c2a9f6b3e526a99189fca19f825dc5148de"; _xsrf=0iZ24KTlaZtUgPN33K6yNCVTzvQY3Z6v; _zap=1e24f181-e31c-4baf-95e4-605d78b6e87e; d_c0="AGCgREkWiQ2PTnsNZcXjRVBTXSdFvQ0DuLg=|1525318055"; __DAYU_PP=Yurv3yV7nNiQ7eQEMUFq6432943dcf11'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'

weburl = 'https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset={offset}&platform=desktop&sort_by=default'
QUESTION_ID = '34011097'
header = {'user_agent': user_agent}

COOKIE = {'cookie': Cookie}

class zhihu(object):
    def __init__(self, offset):
        self.offset = offset
    def gain_data(self):
        url = weburl.format(question_id=QUESTION_ID, offset=self.offset)
        req = requests.get(url, headers=header, cookies=COOKIE)
        jsondata = req.json()
        if not jsondata['paging']['is_end']:
            self.save(jsondata['data'])
            self.offset += 1
            return self.gain_data()
        else:
            print('程序中止')
            return
        
        def save_data(self, jsondata):
            with jlines.open('{}.json'.format(question_id, 'a')) as f:
                for jsonl in jsondata:
                    print(self.offset, jsonl)
                    f.write(jsonl)
                
                
if __name__ == '__main__':
    zhihu(offset=0).gain_data()