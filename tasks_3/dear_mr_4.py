"""
Обращение в письмах начинаются с фразы “Dear Mr./Mrs./Miss/Ms. ...“.
Необходимо определить и вывести пол человека, которому данное письмо
адресовано. Приглашение письма запрашивается у пользователя.
"""

letter = input("Your letter: ")
result = letter.lower().startswith('dear mr.')

if result:
    print("Male")
else:
    print("Female")
