from api_tests.home.get_users_list import ApiTests
from utils import PropertyFile


def main():
    get_url = PropertyFile.getValue('URI', 'list_users')
    get_api_check = ApiTests()
    get_api_check.list_users(get_url)


if __name__ == "__main__":
    main()