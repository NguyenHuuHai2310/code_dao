import json

import brotli
import zlib
import gzip
import requests


class request_fb:

    def make_request(self, params, method, authority, origin, is_referer, referer, user_agent, cookie, is_body, body,
                     is_header=True):
        try:
            headers = {
                'authority': authority,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': origin,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
                'accept-encoding': 'gzip, deflate, br',
                'connection': 'keep-alive',
            }

            if is_referer:
                headers['referer'] = referer

            cookies = {
                'cookie': cookie
            }

            if is_body:
                data = body
            else:
                data = None
            # data = body if is_body else None

            response = requests.request(method, params, headers=headers, cookies=cookies, data=data,
                                        allow_redirects=True)
            # if response.headers.get('Content-Encoding') == 'br':
            #     compressed_data = response.content
            #     uncompressed_data = brotli.decompress(compressed_data)
            #     content = uncompressed_data.decode('utf-8')
            # else:
            #     content = response.text

            hai = response.headers
            hai = response.headers.get('Set-Cookie')
            hai = response.cookies.get_dict()

            van = response.content
            hai_van = response.text
            print(response.text)
            if is_header:
                return str(response.headers) + response.text
            else:
                return response.text

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_approvals_code(self, url):
        try:
            response = requests.request('GET', url, allow_redirects=True, verify=False)
            return response
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi lấy code 2FA!'
            })

    def get_cookie_before_login_facebook_mbasic(self, user_agent):
        try:
            response = self.make_request('https://mbasic.facebook.com/login.php', 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                                         user_agent, '', False, '')
            return response
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })
