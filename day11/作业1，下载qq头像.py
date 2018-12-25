#1、获取到qq号和群名片，如果没有群名片的话，取昵称
#2、根据qq号下载头像
import requests
url='https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
headers = {'cookie':'pt2gguin=o0511402865; RK=JQZpwBp1by; ptcz=6c30e26a9ed6be93d3de9e4c4aca3e55650cf99fcffa64729bd1d58a5fb209d9; pgv_pvi=779236352; pgv_pvid=6970909788; qb_qua=; qb_guid=818de686e29d412fa4ee9e99905ea166; Q-H5-GUID=818de686e29d412fa4ee9e99905ea166; NetType=; pgv_si=s8948704256; uin=o0511402865; skey=@4qrz3B37F; ptisp=cnc; p_uin=o0511402865; pt4_token=UEDJ1b7Mj5a2UdO21KAFwRhg3X*MQ--1ZLvEazYW8zE_; p_skey=MOjeaK1kxuqa6dFa4vq-RdlkG*cyaQ39i-Ju7HQfpf8_'}
data = {"gc":634655327,'st':0,'end':100,'sort':0,'bkn':309096635}
req = requests.post(url,data=data,headers=headers)
mems = req.json().get('mems')#所有的学生信息
for mem in mems:
    file_name = mem.get('card') if mem.get('card') else mem.get("nick")
    qq_num = mem.get('uin')
    #三元表达式
    img_url='https://q4.qlogo.cn/g?b=qq&nk=%s&s=140'%qq_num
    img_content = requests.get(img_url).content
    with open(file_name+'.jpg','wb') as fw:
        fw.write(img_content)



