import vk
import settings
import json
import time

while True:
    session = vk.AuthSession(app_id=settings.vkapp_id, user_login=settings.user_login, user_password=settings.user_pass)
    api = vk.API(session)

    s = api.groups.getRequests(group_id=settings.club_id, count=1)

    json_data = json.dumps(s)
    parsed_json = json.loads(json_data)


    if (parsed_json[:1]==[0]) :
        print('Заявок нет','\n')
    else:
        while parsed_json[:1]!=[0]:
            print('Кол-во заявок: ', parsed_json[:1])

            api.groups.approveRequest(group_id=settings.club_id, user_id=parsed_json[1:])

            s = api.groups.getRequests(group_id=settings.club_id, count=1)
            json_data = json.dumps(s)
            parsed_json = json.loads(json_data)

            time.sleep(3)

    print('============================','\n')
    print('Все заявки приняты!')
    time.sleep(settings.sleep_time)