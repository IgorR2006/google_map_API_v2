import json


class Checking:

    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code, f"Фактический Код ответа, {response.status_code}"
        print(f"Успешно!!! Статус код ответа: {response.status_code}")

    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, f"Часть обязательных полей отсутствует, {list(token)}"
        print("Все обязательные поля присутствуют")

    @staticmethod
    def check_json_token_value(response, filed_name, expected_value):
        token = response.json()
        value = token.get(filed_name)
        assert value == expected_value, f"Содержимое обязательных полей отсутствует, {value}"
        print("Содержимое обязательных полей присутствуют, ", filed_name, " = ", value)
