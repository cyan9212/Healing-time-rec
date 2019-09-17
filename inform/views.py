import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from inform.dialog_flow import get_answer
from inform.message import print_categories
from inform.message import print_shop_info
from inform.message import print_shops
from inform.message import print_review
from inform.message import print_places
from inform.message import print_date_places
from inform.message import print_friend_places


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'content': '안녕하세요 힐링타임 추천 서비스 입니다. 무엇을 도와드릴까요?'
    })


@csrf_exempt
def message(request):
    message = (request.body.decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    intent, answer = get_answer(return_str), ''
    if '주변' in intent:
        answer = print_categories(intent)
    elif '주제' in intent:
        answer = print_shops(intent)
    elif '정보' in intent:
        answer = print_shop_info(intent)
    elif intent.endswith('후기'):
        answer = print_review(intent)
    elif intent == '[empty response]':
        answer = '잘못 알아들었습니다. 제대로 말씀해주세요'
    elif intent.endswith('지역 선택'):
        answer = print_places()
    elif intent.endswith('데이트 추천'):
        answer = print_date_places(intent)
    elif intent.endswith('친구 추천'):
        answer = print_friend_places(intent)
    else:
        answer = intent
    return JsonResponse({
        'message': {
            'text': answer,
        },
        'keyboard': {
            'type': 'text',
        }
    })
