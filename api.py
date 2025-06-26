import requests
import curl


class UserApi:
    @staticmethod
    def create_user_api(user_data):
        creation = requests.post(curl.url_create_user, json=user_data)
        if creation.status_code != 200:
            creation = requests.post(curl.url_create_user, json=user_data)
        return creation

    @staticmethod
    def get_user_token_api(user_data):
        creation = UserApi.create_user_api(user_data)
        token = creation.json().get('accessToken')
        return token

    @staticmethod
    def delete_user_api(token):
        delete_user = requests.delete(curl.url_delete_user, headers={'Authorization': token})
        return delete_user

