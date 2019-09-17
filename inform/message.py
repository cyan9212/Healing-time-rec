import re
import random

from inform.models import Shop
from inform.models import Review


def print_categories(question):
    place, categories = question.split()[0], []
    for shop in Shop.objects.filter(place=place):
        try:
            category = re.findall('(?<=>)\w+', shop.category)[-1]
        except IndexError:
            category = shop.category
        if category not in categories:
            categories.append(category)
    categories = ','.join(categories)
    return '{} 주변에는 '.format(place) + categories + '들이 있어요!!'


def print_shops(question):
    data = question.split()
    place, category = data[0], data[2]
    message = '{} 주변 {} 매장들은 다음과 같이 있어요!!'.format(place, category)
    shops = [shop for shop in Shop.objects.filter(place=place, category__endswith=category)]
    shops = sorted(shops, key=lambda shop: shop.score, reverse=True)
    for shop in shops:
        message += "\n-{} (평점: {}/5)".format(shop.title, shop.score)
    message += '\n궁금하신 매장 이름을 입력해주세요!!'
    # print(message)
    return message


def print_shop_info(question):
    tokens = question.split()
    place, title = tokens[0], ' '.join(tokens[1:-1])
    shops, target = Shop.objects.filter(place=place), None
    for shop in shops:
        if shop.title.replace(' ', '') == title.replace(' ', ''):
            target = shop
            break
    phone_number = target.telephone if target.telephone else '죄송합니다ㅠ 전화번호가 검색되지 않네요'
    message = "{place} 지역 '{title}'의 전화번호와 주소는 다음과 같아요!!" \
              "\n\n[전화번호]\n{telephone}" \
              "\n\n[지도]\n{map_url}" \
              "\n\n가격, 이용 시간 등의 정보는 다음 url을 참조하세요!!" \
              "\n{info_url}".format(place=target.place,
                                    title=target.title,
                                    telephone=phone_number,
                                    map_url=target.address_url,
                                    info_url=target.info_url)
    if len(Review.objects.filter(shop=target)):
        message += "\n\n후기 정보가 궁금하시면 '후기'라고 입력해주세요!!"
    print(message)
    return message


def print_review(question):
    data = question.split()
    shop_title = ' '.join(data[1:-1])
    reviews = Review.objects.filter(title=shop_title)
    if not len(reviews):
        return "죄송합니다. '{}' 매장에는 후기가 아직 없어요ㅜ".format(shop_title)
    print(reviews)
    message = '{shop_title}의 후기들은 다음과 같아요!! 전체보기를 누르시면 보기 편해요!!'.format(shop_title=shop_title)
    for review in reviews:
        changed_review_title = review.review_title.replace('\n', '')
        parenthesises = re.findall('\[.*\]', changed_review_title)
        for parenthesis in parenthesises:
            changed_review_title = changed_review_title.replace(parenthesis, '')
        changed_url = review.url.replace('\n', '')
        message += '\n\n{title}\n{url}'.format(id=review.id, title=changed_review_title,
                                               url=changed_url)
    return message


def print_places():
    return '강남, 홍대, 건대 중에 한 군데를 입력해주시겠어요?'


def print_date_places(question):
    place = question.split()[0]
    message_dict = {'고양이카페': '고양이들과 함께하는 데이트 어떠세요?',
                    '보드카페': '연인과 심심하면 어떡하시냐구요? 다양한 보드게임으로 고민을 해결해보세요!!',
                    '만화방': '좋아하는 연인과 함께 만화책 보기!! 두근두근 하지 않으세요?',
                    'VR': '가상 현실에서도 연인과 함께 해야하지 않을까요?'}
    if place == '홍대':
        message_dict.pop('VR')
    category = random.choice(list(message_dict.keys()))
    message = message_dict[category]
    message += '\n\n' + print_shops(place + ' 주제' + ' {}'.format(category) + ' 목록')
    # print(message)
    return message


def print_friend_places(question):
    place = question.split()[0]
    message_dict = {'보드카페': '친구들과 심심할 때는 보드게임 한 판!! 어떠세요?',
                    'VR': '현실에서의 우정은 가상까지!! VR 체험 한번 가실까요?',
                    '멀티방': '한가지만 하기에는 지루할 때!! 역시 멀티방이죠?'}
    if question.startswith('홍대'):
        message_dict.pop('VR')
    category = random.choice(list(message_dict.keys()))
    message = message_dict[category]
    message += '\n\n' + print_shops(place + ' 주제' + ' {}'.format(category) + ' 목록')
    # print(message)
    return message