import sender_stand_request
import data

# эта функция меняет значения в параметре name
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body




# Функция для позитивной проверки
def positive_assert(name):

    set_body = get_kit_body(name)

    # В переменную set_response сохраняется результат запроса на создание набора:
    set_response = sender_stand_request.post_new_client_set(set_body, sender_stand_request.token)
    # Проверяется, что код ответа равен 201
    assert set_response.status_code == 201
    assert set_response.json()["name"] == name


# Функция для негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную set_token сохраняется токен
    response = sender_stand_request.post_new_client_set(kit_body, sender_stand_request.token)

    assert response.status_code == 400

    assert response.json()["code"] == 400



# Позитивные тесты
# 1
def test_create_set_1_letter_in_name_success_response():
    positive_assert("a")
# 2
def test_create_set_511_letter_in_first_name_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
# 3
def test_create_set_english_letter_in_name_success_response():
    positive_assert("QWErty")
# 4
def test_create_set_russian_letter_in_name_success_response():
    positive_assert("Мария")
# 5
def test_create_set_simbol_in_name_success_response():
    positive_assert("\"№%@\",")
# 6
def test_create_set_space_in_name_success_response():
    positive_assert( " Человек и КО ")
# 7
def test_create_set_namber_in_name_success_response():
    positive_assert( "123")




#Негативные тесты
# 8
def test_create_set_0_letter_in_name_error_response():
    negative_assert_code_400("")
# 9
def test_create_set_512_letter_in_name_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
# 10
def test_create_set_type_number_in_name_error_response():
    negative_assert_code_400(123)

# 11
# В запросе нет параметра name
def test_create_set_no_name_error_response():
    set_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    set_body.pop("name")
    # Проверка полученного ответа
    negative_assert_code_400(set_body)




