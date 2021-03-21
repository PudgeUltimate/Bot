import requests
import vk_api

vk_session = vk_api.VkApi(token='1a915719e4cf8146cc9a8ed2cd9cc46507994c9868dbd5dd4b96af5235e4cbd3d98892c514cfef37ef3af')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    message='ЗАТКНИСЬ'
		)
