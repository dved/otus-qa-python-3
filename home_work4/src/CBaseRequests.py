import requests
from pprint import pp
from time import sleep



class CBaseRequest:
    REQUEST_TYPES = {
        'get': 'GET',
        'post': 'POST',
        'delete': 'DELETE'
    }
    SUCCESS_RESPONSE_CODE = 200

    def __init__(self, base_url):
        # TODO add check if base_ulr contains valid url
        self._base_url = base_url
#        print(f"{list(self.REQUEST_TYPES.values())} ")
#        print(f"{self.SUCCESS_RESPONSE_CODE}")


    def _log_reponse_screen(self, response):
        pp(f'Response URL: {response.url}')
        pp(f'Response Status Code: {response.status_code}')
        pp(f'Response Reason: {response.reason}')
        pp(f'Response Text:')
        pp(response.text)
        pp(f'Response Json Object:')
        pp(response.json())

    def _request(self, url, request_type, data=None, expected_error=None, expected_status_code=200, timeout_requests=0):
        max_retries = 10
        stop_flag = False
        current_retry = 0
        while not stop_flag and current_retry < max_retries:
            if request_type == 'GET':
                print(f'making GET request to {url}')
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, data)
            elif request_type == 'DELETE':
                response = requests.delete(url)
            else:
                print(f"Wrong request_type was passed, Expected one from {list(self.REQUEST_TYPES.values())} Got: {request_type}")
                return None
            # TODO need to think about removing 200 as hardcode
            if not expected_error and response.status_code == self.SUCCESS_RESPONSE_CODE:
                stop_flag = True
            elif expected_error:
                # TODO add checks if method expects error and the response code is the same as expectable
                stop_flag = False
            sleep(timeout_requests)
            current_retry = current_retry + 1

#        self._log_reponse_screen(response)
        return response

    def get(self, endpoint: str, endpoint_id: int = '', filter: str = None, paged: str = None, expected_error=False):
        url = f"{self._base_url}/{endpoint}"
        if endpoint_id:
            url = f"{url}/{endpoint_id}"
        if filter:
            url = f"{url}/?{filter}"
        if paged and filter:
            url = f"{url}&{paged}"
        if paged:
            url = f"{url}?{paged}"
        response = self._request(url,request_type=self.REQUEST_TYPES['get'], expected_error = expected_error)
        if response:
            return response.json()
        else:
            raise ValueError()
