import json

import requests


class anycaptcha:
    def __init__(self, client_key) -> None:
        super().__init__()
        self.client_key = client_key

    def request_anycaptcha_image_to_text(self, params, method, body):
        try:
            headers = {
                'content-type': 'text/plain',
            }
            response = requests.request(method, params, headers=headers, data=body,
                                        allow_redirects=True)

            return response

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def create_task_image_to_text(self, params, method, client_key, image):
        try:
            body = '{       ' \
                   '"clientKey": "' + client_key + '",' \
                                                   '"task": {' \
                                                   '"type": "ImageToTextTask",' \
                                                   '"body": "' + image + '"' \
                                                                         '}' \
                                                                         '}'
            return self.request_anycaptcha_image_to_text(params, method, body)

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })
    def get_task_result_image_to_text(self, params, method, client_key, task_id):
        try:
            body = '{' \
                   '"clientKey": "'+client_key+'",' \
                                               '"taskId": '+task_id+'' \
                                                                    '}'
            return self.request_anycaptcha_image_to_text(params, method, body)

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })
