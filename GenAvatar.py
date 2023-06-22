import json

import requests


class GenFace100K:
    def __init__(self) -> None:
        super().__init__()

    def get_random_url_avatar(self):
        try:
            url = "https://100k-faces.glitch.me/random-image-url"

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            response = json.loads(response.text)
            return json.dumps({
                'status': 200,
                'message': 'Tạo avatar thành công',
                'url': response['url'],
            })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi tạo avatar'
            })
