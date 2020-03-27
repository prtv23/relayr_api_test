import requests


class GetApiReq:

    def get_method(url):
        response = requests.get(url)
        return response


