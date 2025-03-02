import requests,base64,json,hashlib
from Crypto.Cipher import AES
def encrypt(key, text):
    cryptor = AES.new(key.encode('utf8'), AES.MODE_CBC, b'0102030405060708')
    length = 16                    
    count = len(text.encode('utf-8'))     
    if (count % length != 0):
        add = length - (count % length)
    else:
        add = 16             
    pad = chr(add)
    text1 = text + (pad * add)    
    ciphertext = cryptor.encrypt(text1.encode('utf8'))          
    cryptedStr = str(base64.b64encode(ciphertext),encoding='utf-8')
    return cryptedStr
def md5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()
def protect(text):
    return {"params":encrypt('TA3YiYCfY2dDJQgg',encrypt('0CoJUm6Qyw8W8jud',text)),"encSecKey":"84ca47bca10bad09a6b04c5c927ef077d9b9f1e37098aa3eac6ea70eb59df0aa28b691b7e75e4f1f9831754919ea784c8f74fbfadf2898b0be17849fd656060162857830e241aba44991601f137624094c114ea8d17bce815b0cd4e5b8e2fbaba978c6d1d14dc3d1faf852bdd28818031ccdaaa13a6018e1024e2aae98844210"}


s=requests.Session()
header={}
url="https://music.163.com/weapi/login/cellphone"
url2="https://music.163.com/weapi/point/dailyTask"
url3="https://music.163.com/weapi/v1/discovery/recommend/resource"
cookie=input()
tempcookie=input()
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        "Accept-Encoding" : "gzip, deflate",
        "Origin": "https://music.163.com",
        "Referer": "https://music.163.com/discover",
        "Cookie":cookie
        }
headers2 = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        "referer" : "http://music.163.com/",
        "Accept-Encoding" : "gzip, deflate",
        "Cookie":cookie
        }
res=s.post(url=url2,data=protect('{"type":0}'),headers=headers)
object=json.loads(res.text)
if object['code']!=200 and object['code']!=-2:
    print("签到时发生错误："+object['msg'])
else:
    if object['code']==200:
        print("签到成功，经验+"+str(object['point']))
    else:
        print("重复签到")

res=s.post(url=url3,data=protect('{"csrf_token":"'+tempcookie+'"}'),headers=headers)
object=json.loads(res.text,strict=False)
for x in object['recommend']:
    url='https://music.163.com/weapi/v3/playlist/detail?csrf_token='+tempcookie
    data={
        'id':x['id'],
        'n':1000,
        'csrf_token':tempcookie,
    }
    res=s.post(url,protect(json.dumps(data)),headers=headers)
    object=json.loads(res.text,strict=False)
    buffer=[]
    count=0
    for j in object['playlist']['trackIds']:
        data2={}
        data2["action"]="play"
        data2["json"]={}
        data2["json"]["download"]=0
        data2["json"]["end"]="playend"
        data2["json"]["id"]=j["id"]
        data2["json"]["sourceId"]=""
        data2["json"]["time"]="240"
        data2["json"]["type"]="song"
        data2["json"]["wifi"]=0
        buffer.append(data2)
        count+=1
        if count>=310:
            break
    if count>=310:
        break
url = "http://music.163.com/weapi/feedback/weblog"
postdata={
    "logs":json.dumps(buffer)
}
res=s.post(url,protect(json.dumps(postdata)))
object=json.loads(res.text,strict=False)
if object['code']==200:
    print("刷单成功！共"+str(count)+"首")
    exit()
else:
    print("发生错误："+str(object['code'])+object['message'])
    exit(object['code'])
