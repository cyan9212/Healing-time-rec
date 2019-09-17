import json

import requests


def get_answer(text, user_key=123):
    data_send = {
        'query': text,
        'sessionId': user_key,
        'lang': 'ko',
    }

    data_header = {
        'Authorization': 'Bearer 90931529ed9e4c0185e0510227c64642',
        'Content-Type': 'application/json; charset=utf-8'
    }

    dialogflow_url = 'https://api.dialogflow.com/v1/query?v=20150910'

    res = requests.post(dialogflow_url,
                        data=json.dumps(data_send),
                        headers=data_header)

    if res.status_code != requests.codes.ok:
        print(res.status_code)
        return '오류가 발생했습니다.'

    data_receive = res.json()
    answer = data_receive['result']['fulfillment']['speech']

    return answer


if __name__ == "__main__":
    print(get_answer("안녕"))
