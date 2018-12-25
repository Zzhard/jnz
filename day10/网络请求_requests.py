import requests
url='http://www.nnzhp.cn/archives/423'

# res = requests.get(url,params={"k":"v","k1":"v"},
#                    cookies={"sss":"xxxx","xxx":"xxxx"},
#                    headers={"xxx":"xxx","xx":"xxx"}
#                    )
# print(res.text) #返回的是字符串


s='pt2gguin=o0511402865; RK=AZYplDpkew; ptcz=a4a8dc50fc8c0b650976ea60b0b4e00ba81652a7ebf835d600e8a1f949a0f942; pgv_pvid=106035495; pgv_pvi=1348426752; _qpsvr_localtk=0.12252090767355917; pgv_si=s2269966336; uin=o0511402865; skey=@teQdrpq8i; ptisp=cnc; p_uin=o0511402865; pt4_token=T41I973kqWw07LPFgmmMdNT*F*fyPZh9m-1VNS-G-Ik_; p_skey=E1JAxm*da9erQrC5LfPTx7VpMqIBI6hQoS9FTWAUowg_'

res = requests.get(url,params={"k":"v","k1":"v"},
                   headers={"cookie":s}
                   )
# url='http://api.nnzhp.cn/api/user/login'
# res = requests.post(url,data={"username":"niuhanyang",
#                           "passwd":"aA123456"})
# print(res.json()) #返回的就是一个字典
# print(res.text)  #json


# MP3_url='http://qiniuuwmp3.changba.com/1113525663.mp3'
# res = requests.get(MP3_url)
# mp3 = res.content  #返回的二进制内容
# f=open('g.mp3','wb')
# f.write(mp3)
# f.close()
#json
#file
#header
#cookie

# url='http://api.nnzhp.cn/api/file/file_upload'
#
#
# res = requests.post(url,files={'file':open('g.mp3','rb')})
# print(res.json())
url='http://api.nnzhp.cn/api/user/add_stu'

data={"phone":"18612531274","grade":"金牛座","name":"郑重"}
res = requests.post(url,json=data)
print(res.json())