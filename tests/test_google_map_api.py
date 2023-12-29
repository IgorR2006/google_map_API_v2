from utils.api import GoogleMapsApi
from utils.cheking import Checking


class TestCreatePlace:
    place_id = ""

    def test_create_new_place(self):

        print("\n Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        json_post = result_post.json()
        TestCreatePlace.place_id = json_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_token_value(result_post, 'status', 'OK')

    def test_get_create_new_place(self):
        print("\n Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(TestCreatePlace.place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_token_value(result_get, 'address', '29, side layout, cohen 09')

    def test_put_create_new_place(self):
        print("\n Метод PUT")
        result_put = GoogleMapsApi.put_new_place(TestCreatePlace.place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_token_value(result_put, 'msg', 'Address successfully updated')

    def test_get_after_put_create_new_place(self):
        print("\n Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(TestCreatePlace.place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(
            result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        )
        Checking.check_json_token_value(result_get, 'address', '100 Lenina street, RU')

    def test_delete_create_new_place(self):
        print("\n Метод DELETE")
        result_del = GoogleMapsApi.del_new_place(TestCreatePlace.place_id)
        Checking.check_status_code(result_del, 200)
        Checking.check_json_token(result_del, ['status'])
        Checking.check_json_token_value(result_del, 'status', 'OK')

    def test_get_after_del_create_new_place(self):
        print("\n Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(TestCreatePlace.place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_token_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")

