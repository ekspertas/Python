# Функция вывода данных пользователя

def user_data_output(name, surname, year_of_birth, city, mail, phone):
    print(f'Имя:', name, '. Фамилия:', surname, '. Год рождения:', year_of_birth,
          '. Город проживания:', city, '. Електронная почта:', mail, '. Номер телефона:', phone)


user_name = input('Ваше имя: ')
user_surname = input('Ваша фамилия: ')
user_year_of_birth = input('Год рождения: ')
user_city = input('Город проживания: ')
user_mail = input('Електронная почта: ')
user_phone = input('Номер телефона: ')

user_data_output(name=user_name, surname=user_surname, year_of_birth=user_year_of_birth,
                 city=user_city, mail=user_mail, phone=user_phone)
