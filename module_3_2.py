def send_email(message, recipient, sender="university.help@gmail.com"):
    #проверяем наличие @ в переменной recipient, а потом в sender, а также, с помощью метода
    #.endswith  проверяем окончания почты.
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    #проверяем равны ли значения sender и recipient
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    # проверяем адрес отправителя, по умолчанию он или нет
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
#выводим всё, что проверяем
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
