import json
from api_methods.home.get_request import GetApiReq
from api_pages.home.get_api_pages import GetApiPages


class ApiTests:

    def list_users(self, url):
        # API URI
        response = GetApiReq.get_method(url)

        # verify api response code to be 200
        tc_res_one = GetApiPages.verify_status_codes(response.status_code)
        assert True == tc_res_one

        # verify total pages to be appropriate
        # parse response to JSON format
        json_response = json.loads(response.text)
        tc_res_two = GetApiPages.verify_total_pages(json_response)
        assert True == tc_res_two

        # verify email displayed in the response is appropriate
        tc_res_three = GetApiPages.verify_email(json_response)
        assert True == tc_res_three