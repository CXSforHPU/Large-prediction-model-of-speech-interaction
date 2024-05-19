"""
作者 河南理工大学 曹显嵩
    河南理工大学 吴锡煐
    本文件使用百度的语音转文本，但效果不尽人意，因为时间关系，没有时间进行更改。
    后续方向可以考虑 讯飞星活，或其他api，只要能够完成语音转文本的功能便够
    或是本地部署

"""


import requests
import json


API_KEY = ""
SECRET_KEY = ""

import base64


def ToBase64(file):

    with open(file, 'rb') as fileObj:
        audio_data = fileObj.read()


    base64_data = base64.b64encode(audio_data)

    return str(base64_data,encoding='utf8'),len(audio_data)




def audio_text(file=None):

    base64_data,num = ToBase64(file)


    url = "https://vop.baidu.com/server_api"

    payload = json.dumps({
        "format": "pcm",
        "rate": 16000,
        "channel": 1,
        "cuid": "KUIWP57Tgh7Fi8cSxBzIstBQMuHZRMmJ",
        "token": get_access_token(),
        "speech":base64_data,
        'len' : num
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return str(response.json()['result'])


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    print(audio_text('temp.wav'))
