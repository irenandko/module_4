# 3.2 "ВК бот с дз сразу"

# import vk_api
# import requests
#
#
# token='vk1.a.C2BmgJzhaIkmjGSbf6FVfv3NhqFm9tmRio8t5jegRUhF16UqS-oCTTs-pegMXDEeDfe35T6Ef5JCq46eiVAaXTAgSM_qdhSnvb6gath7LlozcoyMVj6yT3UAQRoO0Bfm1c7HCZUygL5Ki0_QxMd9p6yIDtXvMrqwvAwhDTy3sUCcjIYIwwiX43xMYLaPcUdNcGgSPI6b7nzs0vvDDbU1xw'
# api = vk_api.VkApi(token=token)
# url = 'https://swapi.dev/api/planets'
# response = requests.get(url)
# b_soup = response.json()
#
# url1 = 'https://swapi.dev/api/starships'
# response_1 = requests.get(url1)
# bb_soup = response_1.json()
#
# def largest_planet():
#     largest = b_soup['results'][0]
#     for planet in b_soup['results']:
#         if int(planet['diameter']) > int(largest['diameter']):
#             largest_planet_ans = planet
#     return largest_planet_ans['name']
#
# def max_speed_starship():
#     fastest = bb_soup['results'][0]
#     for starship in bb_soup['results']:
#         if starship['max_atmosphering_speed']!='n/a' and fastest['max_atmosphering_speed']!='n/a' and not 'km' in starship['max_atmosphering_speed'] and not 'km' in fastest['max_atmosphering_speed']:
#             if int(starship['max_atmosphering_speed']) > int(fastest['max_atmosphering_speed']):
#                 fastest_starship_ans = starship
#     return fastest_starship_ans['name']
#
# ans_planet = largest_planet()
# ans_starship =max_speed_starship()
#
# while True:     # здесь нет функции ловли сообщений как в телеге, приходится старым способом проверки лимита и отслеживал все сообщения (постоянная работа)
#     messages_find = api.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages_find['count']>=1:
#         print(messages_find)
#         user_id = messages_find['items'][0]['last_message']['from_id']
#         message_id = messages_find['items'][0]['last_message']['id']
#         messages_text = messages_find['items'][0]['last_message']['text']
#         if messages_text.lower()=='привет':
#             api.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'hello'})
#         elif messages_text.lower()=='планеты':
#             api.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message':'The largest planet - '+ ans_planet })
#         elif messages_text.lower()=='корабли':
#             api.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message':'The fastest starship - '+ ans_starship })
#         else:
#             api.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'send greeting'})
#


# 3.3 "ВК бот и удаленный сервер"  longpolling - отправляет сообщение не сразу, а после  определенного события или истечения времени
#
# import vk_api
# from vk_api.longpoll import VkLongPoll, VkEventType
# import requests
# from bs4 import BeautifulSoup
#
# def get_course(id):
#     url='https://www.cbr.ru/scripts/XML_daily.asp?date_req=11/07/2023'
#     response= requests.get(url)
#     xml = BeautifulSoup(response.content, 'html.parser')
#     valute = xml.find('valute', {'id':id})
#     value = valute.value.text
#     return value
#
# valute = ['доллар','евро','юань','вона']
# valute_id = ['R01235',"R01239","R01375","R01815"]
#
# token = 'vk1.a.99NYRpTM0rWNCa6-DfDKbV6ureyYMMeUFSK5L7ZB8pG-YT21Q0Ez8edYBuuxpaMmdEnYkNvOHZwpdpxEwwaRwfhFdK_FZlIjJro2esqUB7e0VezY8eKfS8WyqG09ZhvUl7AWgwk8B8Lo8Ef3p3KCT_zgspfFRgMy_NwLwnHdbDdA8wYAcJZAKVrVUG-O_R3EXwfMTIV37NC7ZgigFRqCZQ'
# vk_session = vk_api.VkApi(token=token)
#
# longpoll = VkLongPoll(vk_session)
# # listen - присылает любые действия в диалоге(от написания сообщения до отправки и удаления)
#
#
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         msg = event.text
#         user_id = event.user_id
#         msg_id = event.message_id
#         if msg.lower()=='привет':
#             vk_session.method('messages.send', {'peer_id': user_id, 'random_id': msg_id, 'message': 'Здарова, отец...\n'
#                                                                             'Чтобы узнать курс определенной валюты, напиши "-к"'})
#         if msg.lower() == '-к':
#             vk_session.method('messages.send',{'peer_id': user_id, 'random_id': msg_id, 'message': 'Курс какой валюты вы хотите узнать?\n'
#                                                                                                    'доллар, евро, юань, вона'})
#         if msg.lower()=='доллар' or msg.lower()=='евро' or msg.lower()=='юань' or msg.lower()=='вона' :
#             vk_session.method('messages.send', {'peer_id': user_id, 'random_id': msg_id,'message':'Сегодня '+ msg.lower() + " стоит " +get_course(valute_id[valute.index(msg)])+' рублей' })
#
#         else:
#             vk_session.method('messages.send', {'peer_id': user_id, 'random_id': msg_id, 'message': 'Я тебя не понимаю, брат'})
#
# get_course(valute_id[int(valute.index(msg[3:]))])




# 4.1 GIT (начало проекта)

# пример оптимизации кода без вложенных циклов, соответственно, ассимптотическая сложность кода гораздо меньше и не приведет к виду n**2, если все символы уникальны
# s = 'aab'
# syms_count = {}
# for syms in s:
#     syms_count[syms]=syms_count.get(syms,0)+1
#
# print(syms_count)
















