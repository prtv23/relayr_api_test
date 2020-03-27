from utils import StatusCodes
from api_data.home.get_api_data import GetApiData
import jsonpath


class GetApiPages:

    def verify_status_codes(status):

        if status == GetApiData.success_status_code:
            print("Test Case to verify, Status Codes PASS")
            return True
        else:
            error = StatusCodes.stagger(status)
            auth_error = str(error)
            print("Authorization Fault :" + " " + str(status) + " : " + auth_error)
            return False

    def verify_total_pages(json_resp):
        # fetch 'page' value using JSON path
        page = jsonpath.jsonpath(json_resp, 'page')
        if page[0] == GetApiData.page_count:
            print("Test Case to verify, Total Pages PASS")
            return True
        else:
            return False

    def verify_email(json_resp):
        # fetch the first dictionary in the list of dictionaries
        email = jsonpath.jsonpath(json_resp, 'data[0]')
        if email[0]['email'] == GetApiData.email:
            print("Test Case to verify, Email Address PASS")
            return True
        else:
            return False
