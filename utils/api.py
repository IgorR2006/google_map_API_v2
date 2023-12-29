from utils.httpmethods import HttpMethods


BASE_URL = "https://rahulshettyacademy.com/maps/api/place/"
KEY = "?key=qaclick123"


class GoogleMapsApi:

    @staticmethod
    def create_new_place():

        json_data = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        post_resource = "add/json"

        post_url = f"{BASE_URL}{post_resource}{KEY}"
        print("Адрес запроса: ", post_url)

        result_post = HttpMethods.post(post_url, json_data)
        print("Тело ответа: ", result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):

        get_resource = "get/json"

        get_url = f"{BASE_URL}{get_resource}{KEY}&place_id={place_id}"
        print("Адрес запроса: ", get_url)

        result_get = HttpMethods.get(get_url)
        print("Тело ответа: ", result_get.text)
        return result_get

    @staticmethod
    def put_new_place(place_id):

        put_resource = "update/json"

        put_url = f"{BASE_URL}{put_resource}{KEY}"
        json_data_upd = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        print("Адрес запроса: ", put_url)

        result_put = HttpMethods.put(put_url, json_data_upd)
        print("Тело ответа: ", result_put.text)
        return result_put

    @staticmethod
    def del_new_place(place_id):

        del_resource = "delete/json"
        del_url = f"{BASE_URL}{del_resource}{KEY}"

        json_data_del = {
            "place_id": place_id,

        }

        print("Адрес запроса: ", del_url)

        result_del = HttpMethods.delete(del_url, json_data_del)
        print("Тело ответа: ", result_del.text)
        return result_del
