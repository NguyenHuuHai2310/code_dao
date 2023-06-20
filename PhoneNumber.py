import json

import requests


class viotp:
    def __init__(self, token) -> None:
        super().__init__()
        self.token = token

    def request_viotp_request_service(self, token, serviceId):
        try:
            response = requests.request('GET',
                                        'https://api.viotp.com/request/getv2?token=' + token + '&serviceId=' + str(serviceId),
                                        allow_redirects=True)

            return response.text

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def request_viotp_get_code(self, token, requestId):
        try:
            response = requests.request('GET',
                                        'https://api.viotp.com/session/getv2?requestId=' + str(requestId) + '&token=' + token,
                                        allow_redirects=True)

            return response.text

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })
