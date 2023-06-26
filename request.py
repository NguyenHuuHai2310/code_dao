import base64
import json
import random
import re
from urllib.parse import urlencode, quote

from GenAvatar import GenFace100K
from create_passport import passport
from captcha import anycaptcha
from PhoneNumber import viotp

import brotli
import zlib
import gzip
import requests


class request_fb:

    def __init__(self, client_key, token, access_token_fb, option_XMDT) -> None:
        super().__init__()
        self.client_key = client_key
        self.token = token
        self.access_token_fb = access_token_fb
        self.option_XMDT = option_XMDT

    def make_request(self, params, method, authority, origin, is_referer, referer, user_agent, cookie, is_body, body,
                     is_header=True):
        try:
            headers = {
                'authority': authority,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
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

            # cookies = cookie

            if is_body:
                data = body
            else:
                data = None
            # data = body if is_body else None

            response = requests.request(method, params, headers=headers, data=data,
                                        allow_redirects=True)
            # if response.headers.get('Content-Encoding') == 'br':
            #     compressed_data = response.content
            #     uncompressed_data = brotli.decompress(compressed_data)
            #     content = uncompressed_data.decode('utf-8')
            # else:
            #     content = response.text

            # hai = response.headers
            # hai = response.headers.get('Set-Cookie')
            # hai = response.cookies.get_dict()

            return response
            # if is_header:
            #     return str(response.headers) + response.text
            # else:
            #     return response.text

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_approvals_code(self, url):
        try:
            response = requests.request('GET', url, allow_redirects=True)
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
            if response.text.__contains__('accept_only_essential'):
                pattern = r'name=\"lsd\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                lsd = matchs[1]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[1]
                referer = response.headers.get('Referer')
                body = 'jazoest=' + quote(jazoest, safe="") + '&lsd=' + quote(lsd, safe="") + '&accept_only_essential=1'

                response = self.make_request(
                    'https://mbasic.facebook.com/cookie/consent/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php',
                    'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                    'https://mbasic.facebook.com/cookie/consent_prompt/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php&refsrc=deprecated&_rdr',
                    user_agent, '', True, body)

                cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                response = self.make_request('https://mbasic.facebook.com/login.php?_rdr', 'GET',
                                             'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                             'https://mbasic.facebook.com/cookie/consent_prompt/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2Flogin.php&refsrc=deprecated&_rdr',
                                             user_agent, cookies, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if cookies != '':
                pattern = r'name=\"lsd\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                lsd = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"m_ts\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                m_ts = matchs[0]
                pattern = r'name=\"li\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                li = matchs[0]
                pattern = r'name=\"bi_xrwh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                bi_xrwh = matchs[0]
                pattern = r'input value=\"([^"]*)\" type=\"submit\" name=\"login\"'
                matchs = re.findall(pattern, response.text)
                login = matchs[0]
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'lsd': lsd,
                    'jazoest': jazoest,
                    'm_ts': m_ts,
                    'li': li,
                    'bi_xrwh': bi_xrwh,
                    'login': login,
                    'message': 'Đăng nhập...!',
                })
            else:
                return json.dumps({
                    'status': 400,
                    'message': 'Login lỗi!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_cookie_checkpoint_2fa(self, id_fb, pass_fb, cookie, lsd, jazoest, m_ts, li, login, bi_xrwh, user_agent):
        try:
            body = 'lsd=' + quote(lsd, safe="") + '&jazoest=' + quote(jazoest, safe="") + '&m_ts=' + quote(m_ts,
                                                                                                           safe="") + '&li=' + quote(
                li, safe="") + '&try_number=0&unrecognized_tries=0&email=' + quote(id_fb, safe="") + '&pass=' + quote(
                pass_fb, safe="") + '&login=' + quote(login, safe="") + '&bi_xrwh=' + quote(bi_xrwh, safe="")
            response = self.make_request(
                'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=9',
                'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                'https://mbasic.facebook.com/login.php', user_agent, cookie, True,
                body)

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if cookies != '':
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Get code 2FA',
                })
            else:
                return json.dumps({
                    'status': 400,
                    'message': 'Login lỗi!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def check_approvals_code(self, cookie, code_2fa, user_agent):
        try:
            response = self.make_request('https://mbasic.facebook.com/checkpoint/?_rdr', 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login.php', user_agent, cookie, False, '')

            flag = response.text.__contains__('approvals_code')
            if flag:
                cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[0][1]
                submit_value = matchs[0][0]
                # get code 2fa
                url = "https://2fa.live/tok/" + re.sub(r'\s+', '', code_2fa)
                response_approvals_code = json.loads(self.get_approvals_code(url).text)
                approvals_code = response_approvals_code['token']
                if len(code_2fa) < 13:
                    return json.dumps({
                        'status': 404,
                        'message': '2fa bị sai!'
                    })
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'nh': nh,
                    'approvals_code': approvals_code,
                    'submit_name': submit_name,
                    'submit_value': submit_value,
                    'message': 'Submit code 2FA: ' + approvals_code,
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Lỗi vượt 2FA!'
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_code_2fa(self, fb_dtsg, jazoest, approvals_code, nh, cookie, user_agent, submit_name, submit_value):
        try:
            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&checkpoint_data=&approvals_code=' + quote(
                approvals_code, safe="") + '&codes_submitted=0&submit%5B' + submit_name + '%5D=' + quote(submit_value,
                                                                                                         safe="") + '&nh=' + quote(
                nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest, safe="")
            response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/checkpoint/?_rdr', user_agent, cookie, True, body)

            flag = response.text.__contains__('name_action_selected')
            if flag:
                cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[0][1]
                submit_value = matchs[0][0]
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'nh': nh,
                    'submit_name': submit_name,
                    'submit_value': submit_value,
                    'message': 'Đang đăng nhập...',
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Đăng nhập thất bại!'
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_cookie_dont_save_browser(self, fb_dtsg, jazoest, nh, cookie, user_agent, submit_name, submit_value):
        try:
            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&checkpoint_data=&name_action_selected=dont_save&submit%5B' + submit_name + '%5D=' + quote(
                submit_value, safe="") + '&nh=' + quote(nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg,
                                                                                           safe="") + '&jazoest=' + quote(
                fb_dtsg, safe="")
            response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookie, True,
                                         body)

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if response.text.__contains__('checkpointSubmitButton-actual-button'):
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[0][1]
                submit_value = matchs[0][0]
                return json.dumps({
                    'status': 302,
                    'cookie': cookies,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'nh': nh,
                    'submit_name': submit_name,
                    'submit_value': submit_value,
                    'message': 'Đang đăng nhập...',
                })
            elif response.text.__contains__('Disagree With Decision'):
                return json.dumps({
                    'status': 404,
                    'message': 'Tài khoản bị checkpoint!'
                })
            else:
                previous_cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.history[0].cookies])
                cookies = previous_cookie + '; ' + cookies
                # if len(response.history):
                #     previous_cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.history[0].cookies])
                #     response = self.make_request('https://mbasic.facebook.com/home.php?refsrc=deprecated&_rdr', 'GET',
                #                                  'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                #                                  'https://mbasic.facebook.com/login/checkpoint/', user_agent, 'checkpoint=deleted; '+previous_cookie,
                #                                  False, '')
                #     previous_cookie = previous_cookie + '; ' + '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                #     if len(response.history):
                #         response = self.make_request('https://mbasic.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2Fhome.php%3Frefsrc%3Ddeprecated&refsrc=deprecated&_rdr',
                #                                      'GET',
                #                                      'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                #                                      'https://mbasic.facebook.com/login/checkpoint/', user_agent,
                #                                      previous_cookie,
                #                                      False, '')
                #         previous_cookie = previous_cookie + '; ' + '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                #         cookies = cookies + '; ' + previous_cookie

                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đăng nhập thành công!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def review_recent_login(self, fb_dtsg, jazoest, nh, cookie, user_agent, submit_name, submit_value):
        try:
            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&checkpoint_data=&submit%5B' + submit_name + '%5D=' + quote(
                submit_value, safe="") + '&nh=' + quote(nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg,
                                                                                           safe="") + '&jazoest=' + quote(
                jazoest, safe="")
            response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookie, True,
                                         body)

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if response.text.__contains__('checkpointSubmitButton-actual-button'):
                pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                fb_dtsg = matchs[0]
                pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                jazoest = matchs[0]
                pattern = r'name=\"nh\" value=\"(.*?)\"'
                matchs = re.findall(pattern, response.text)
                nh = matchs[0]
                pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                matchs = re.findall(pattern, response.text)
                submit_name = matchs[1][1]
                submit_value = matchs[1][0]
                # This is me
                body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                                  safe="") + '&checkpoint_data=&submit%5B' + submit_name + '%5D=' + quote(
                    submit_value, safe="") + '&nh=' + quote(nh, safe="") + '&fb_dtsg=' + quote(fb_dtsg,
                                                                                               safe="") + '&jazoest=' + quote(
                    jazoest, safe="")
                response = self.make_request('https://mbasic.facebook.com/login/checkpoint/', 'POST',
                                             'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                             'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookies, True,
                                             body)
                if response.text.__contains__('name_action_selected'):
                    cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
                    pattern = r'name=\"fb_dtsg\" value=\"(.*?)\"'
                    matchs = re.findall(pattern, response.text)
                    fb_dtsg = matchs[0]
                    pattern = r'name=\"jazoest\" value=\"(.*?)\"'
                    matchs = re.findall(pattern, response.text)
                    jazoest = matchs[0]
                    pattern = r'name=\"nh\" value=\"(.*?)\"'
                    matchs = re.findall(pattern, response.text)
                    nh = matchs[0]
                    pattern = r'input value=\"(.*?)\" type=\"submit\" name=\"submit\[(.*?)\]\"'
                    matchs = re.findall(pattern, response.text)
                    submit_name = matchs[0][1]
                    submit_value = matchs[0][0]
                    # Submit don't save browser
                    response = self.get_cookie_dont_save_browser(fb_dtsg, jazoest, nh, cookies, user_agent, submit_name,
                                                                 submit_value)
                    return response
                else:
                    return json.dumps({
                        'status': 404,
                        'message': 'Đăng nhập thất bại!',
                    })
            else:
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đang đăng nhập...',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def check_login_to_home(self, cookie, user_agent):
        try:
            response = self.make_request('https://mbasic.facebook.com/home.php?refsrc=deprecated&_rdr', 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         'https://mbasic.facebook.com/login/checkpoint/', user_agent, cookie, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            if cookies != '':
                if str(cookie).__contains__('checkpoint=deleted'):
                    cookies = cookies + str(cookie).replace('checkpoint=deleted', '')
                else:
                    cookies = cookies + cookie
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đăng nhập thành công!',
                })
            else:
                return json.dumps({
                    'status': 400,
                    'message': 'Đăng nhập thất bại!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def check_account_quality(self, id_fb, cookie, user_agent):
        try:
            response = self.make_request('https://www.facebook.com/accountquality/' + id_fb + '/?source=link', 'GET',
                                         'www.facebook.com', 'https://www.facebook.com', True,
                                         'https://www.facebook.com/accountquality',
                                         user_agent, cookie, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            pattern = r'"token":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            lsd = matchs[1]
            pattern = r'"sessionID":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            session_id = matchs[0]
            pattern = r'"haste_session":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            haste_session = matchs[0]
            pattern = r'"connectionClass":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            __ccg = matchs[0]
            pattern = r'"server_revision":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            __rev = matchs[0]
            pattern = r'"hsi":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            __hsi = matchs[0]
            pattern = r'"token":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'"__spin_r":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            __spin_r = matchs[0]
            pattern = r'"__spin_b":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            __spin_b = matchs[0]
            pattern = r'"__spin_t":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            __spin_t = matchs[0]

            headers = {
                'authority': 'www.facebook.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/accountquality/' + id_fb,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent,
                'x-asbd-id': '198387',
                'x-fb-friendly-name': 'AccountQualityHubAssetOwnerViewV2Query',
                'x-fb-lsd': lsd,
                'accept-encoding': 'gzip, deflate, br',
                'connection': 'keep-alive',
            }

            data = 'av=' + quote(id_fb, safe="") + '&session_id=' + quote(session_id, safe="") + '&__user=' + quote(
                id_fb, safe="") + '&__a=1&__req=1&__hs=' + quote(haste_session, safe="") + '&dpr=2&__ccg=' + quote(
                __ccg, safe="") + '&__rev=' + quote(__rev, safe="") + '&__s=ma0z7e%3A573g7w%3Adpehmi&__hsi=' + quote(
                __hsi,
                safe="") + '&__dyn=7xeUmxa2C5rgydwn8K2abBWqxu59o9E4a2i5VGxK5FEG484S4UKewPGi4FoixWE-16xq4EOezobo-4Lxe1kx21FxG9xedz8hwgo5qq3a4EuCx62a2q5E9UeUryFE4WWBBwLjzu2SJaECfiwzlwXyXwBxu1UxO6AcK2y5oeEjx63K7EC11xnzoO9ws8nw8ScwgECu7EK3i2a3Fe6rwiolDwFwBgaohzE8U98doK78-4Ea8mwnHxJUpx2aK2a4p8y26U8U-UbE4S7VEjCx6Etw9O3ifzobEaUiwm8myUnwUzpA6EfEO32fxiFVoa9obGwgUy1kx6bCyVUCcG2-qaUK2e0UFU2RwiU8U6Ci2G1bzFHwCwmo4S7EaUkw&__csr=&fb_dtsg=' + quote(
                fb_dtsg, safe="") + '&jazoest=25769&lsd=' + quote(lsd, safe="") + '&__spin_r=' + quote(__spin_r,
                                                                                                       safe="") + '&__spin_b=' + quote(
                __spin_b, safe="") + '&__spin_t=' + quote(__spin_t,
                                                          safe="") + '&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=AccountQualityHubAssetOwnerViewV2Query&variables=%7B%22assetOwnerId%22%3A%22' + quote(
                id_fb, safe="") + '%22%7D&server_timestamps=true&doc_id=6139497919470985'

            response = requests.request('POST', 'https://www.facebook.com/api/graphql/', headers=headers, data=data,
                                        allow_redirects=True)
            response = json.loads(response.text)
            acc_is_restricted = response['data']['assetOwnerData']['advertising_restriction_info']['is_restricted']
            if acc_is_restricted:
                return json.dumps({
                    'status': 200,
                    'acc_is_restricted': acc_is_restricted,
                    'message': 'Tài khoản cần XMDT',
                })
            else:
                return json.dumps({
                    'status': 200,
                    'acc_is_restricted': acc_is_restricted,
                    'message': 'Tài khoản không bị XMDT',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_view_checkpoint_282(self, cookie, user_agent):
        try:
            response = self.make_request(
                'https://www.facebook.com/accountquality/advertising_access/?callsite=15&enforcement=1&intent=1',
                'GET',
                'www.facebook.com', 'https://www.facebook.com', False, '',
                user_agent, cookie, False, '')
            pattern = r'https:\/\/www.facebook.com\/checkpoint\/[0-9]+\/([0-9]+)'
            matchs = re.findall(pattern, response.history[0].headers.get('Location'))
            number_checkpoint = matchs[0]

            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            # Upload your ID
            if response.text.__contains__('mobile_image_data'):
                return json.dumps({
                    'status': 200,
                    'action': 'upload_your_id',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Upload your id',
                })
            # Starting process to request a review
            elif response.text.__contains__('action_proceed'):
                return json.dumps({
                    'status': 200,
                    'action': 'action_proceed',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Bắt đầu XMDT',
                })
            # Captcha
            elif response.text.__contains__('captcha_response'):
                return json.dumps({
                    'status': 200,
                    'action': 'captcha',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Giải captcha',
                })
            # View input phone number
            elif response.text.__contains__('contact_point'):
                return json.dumps({
                    'status': 200,
                    'action': 'add_phone_number',
                    'number_checkpoint': number_checkpoint,
                    'message': 'Thêm SĐT',
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Không tìm thấy link XMDT!',
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_continue_checkpoint(self, number_checkpoint, cookie, user_agent):
        try:
            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
            matchs = re.findall(pattern, response.text)
            params = 'https://mbasic.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
            pattern = r'name="fb_dtsg"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'name="jazoest"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            jazoest = matchs[0]
            pattern = r'value="([^"]+)"\s+type="submit"\s+name="action_proceed"'
            matchs = re.findall(pattern, response.text)
            action_proceed = matchs[0]

            body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                              safe="") + '&action_proceed=' + quote(
                action_proceed, safe="")
            response = self.make_request(params,
                                         'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         referer, user_agent, cookie, True, body)
            return self.submit_code_checkpoint(number_checkpoint, cookie, user_agent, self.client_key)

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_code_checkpoint(self, number_checkpoint, cookie, user_agent, client_key):
        try:
            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
            matchs = re.findall(pattern, response.text)
            params = 'https://mbasic.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
            pattern = r'name="fb_dtsg"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'name="jazoest"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            jazoest = matchs[0]
            pattern = r'name="captcha_persist_data"\s+value="([a-zA-Z0-9_-]+)"'
            matchs = re.findall(pattern, response.text)
            captcha_persist_data = matchs[0]
            pattern = r'value="([^"]+)"\s+type="submit"\s+name="action_submit_bot_captcha_response"'
            matchs = re.findall(pattern, response.text)
            action_submit_bot_captcha_response = matchs[0]
            pattern = r'https:\/\/mbasic\.facebook\.com\/captcha\/tfbimage\.php\?captcha_challenge_code=([a-zA-Z0-9_-]+)&amp;captcha_challenge_hash=([a-zA-Z0-9_-]+)'
            matchs = re.findall(pattern, response.text)
            url_image_captcha = 'https://mbasic.facebook.com/captcha/tfbimage.php?captcha_challenge_code=' + matchs[0][
                0] + '&captcha_challenge_hash=' + matchs[0][1]
            response = self.make_request(url_image_captcha, 'GET',
                                         'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                         referer, user_agent, cookie, False, '')
            # Encode the image string data into base64
            image = base64.b64encode(response.content).decode('utf-8')
            # resolve captcha
            captcha = anycaptcha(client_key)
            response_captcha = captcha.create_task_image_to_text('https://api.anycaptcha.com/createTask', 'POST',
                                                                 client_key, image)
            response_captcha = json.loads(response_captcha)
            if response_captcha['errorId'] == 0:
                response_captcha = captcha.get_task_result_image_to_text('https://api.anycaptcha.com/getTaskResult',
                                                                         'POST', client_key, response_captcha['taskId'])
                response_captcha = json.loads(response_captcha)
                if response_captcha['errorId'] == 0:
                    while response_captcha['status'] == 'processing':
                        response_captcha = captcha.get_task_result_image_to_text(
                            'https://api.anycaptcha.com/getTaskResult', 'POST', client_key, response_captcha['taskId'])
                        response_captcha = json.loads(response_captcha)
                    captcha_response = response_captcha['solution']['text']
                    body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                                      safe="") + '&captcha_persist_data=' + quote(
                        captcha_persist_data, safe="") + '&captcha_response=' + quote(captcha_response,
                                                                                      safe="") + '&action_submit_bot_captcha_response=' + quote(
                        action_submit_bot_captcha_response, safe="")
                    response = self.make_request(params,
                                                 'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                                 referer, user_agent, cookie, True, body)
                    return self.submit_phone_number(number_checkpoint, cookie, user_agent, self.token, 7)
                else:
                    return json.dumps({
                        'status': 404,
                        'message': 'Giải captcha lỗi!'
                    })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Giải captcha lỗi!'
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_phone_number(self, number_checkpoint, cookie, user_agent, token, serviceId):
        try:
            response = self.make_request(
                'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
            matchs = re.findall(pattern, response.text)
            params = 'https://mbasic.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
            pattern = r'name="fb_dtsg"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'name="jazoest"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            jazoest = matchs[0]
            pattern = r'value="([^"]+)"\s+type="submit"\s+name="action_set_contact_point"'
            matchs = re.findall(pattern, response.text)
            action_set_contact_point = matchs[0]

            # get phone number from api
            phone_number = viotp(token)
            response_phone_number = phone_number.request_viotp_request_service(token, serviceId)
            response_phone_number = json.loads(response_phone_number)
            if response_phone_number['status_code'] == 200:
                contact_point = response_phone_number['data']['phone_number']
                requestId = response_phone_number['data']['request_id']
                body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                                  safe="") + '&country_code=VN&contact_point=' + quote(
                    contact_point, safe="") + '&action_set_contact_point=' + quote(action_set_contact_point, safe="")
                response = self.make_request(params,
                                             'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                             referer, user_agent, cookie, True, body)
                response = self.make_request(
                    'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                    'GET',
                    'mbasic.facebook.com', 'https://mbasic.facebook.com', False, '',
                    user_agent, cookie, False, '')
                referer = 'https://mbasic.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
                if response.text.__contains__('action_submit_code'):
                    # get code from phone number
                    response_phone_number = phone_number.request_viotp_get_code(token, requestId)
                    response_phone_number = json.loads(response_phone_number)
                    if (response_phone_number['status_code'] == 200) and (response_phone_number['data']['Status'] != 2):
                        while response_phone_number['data']['Status'] == 0:
                            response_phone_number = phone_number.request_viotp_get_code(token, requestId)
                            response_phone_number = json.loads(response_phone_number)
                        code = response_phone_number['data']['Code']

                        pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
                        matchs = re.findall(pattern, response.text)
                        params = 'https://mbasic.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
                        pattern = r'name="fb_dtsg"\s+value="(.*?)"'
                        matchs = re.findall(pattern, response.text)
                        fb_dtsg = matchs[0]
                        pattern = r'name="jazoest"\s+value="(.*?)"'
                        matchs = re.findall(pattern, response.text)
                        jazoest = matchs[0]
                        pattern = r'value="([^"]+)"\s+type="submit"\s+name="action_submit_code"'
                        matchs = re.findall(pattern, response.text)
                        action_submit_code = matchs[0]

                        body = 'fb_dtsg=' + quote(fb_dtsg, safe="") + '&jazoest=' + quote(jazoest,
                                                                                          safe="") + '&code=' + quote(
                            code, safe="") + '&action_submit_code=' + quote(action_submit_code, safe="")
                        response = self.make_request(params,
                                                     'POST', 'mbasic.facebook.com', 'https://mbasic.facebook.com', True,
                                                     referer, user_agent, cookie, True, body)
                        return self.submit_your_id(number_checkpoint, cookie, user_agent, self.access_token_fb,
                                                   self.option_XMDT['option_choise_Phoi'])
                    else:
                        return json.dumps({
                            'status': 404,
                            'message': 'Lấy code gửi về SĐT thất bại!'
                        })
                else:
                    return json.dumps({
                        'status': 404,
                        'message': 'Thêm SĐT thất bại!'
                    })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Lấy SĐT thất bại!'
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def submit_your_id(self, number_checkpoint, cookie, user_agent, access_token_fb, option_choise_Phoi):
        try:
            response = self.make_request(
                'https://m.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F',
                'GET',
                'm.facebook.com', 'https://m.facebook.com', False, '',
                user_agent, cookie, False, '')
            referer = 'https://m.facebook.com/checkpoint/1501092823525282/' + number_checkpoint + '/?next=%2Faccountquality%2F'
            pattern = r'form\s+method="[^"]+"\s+action="\/checkpoint([^"]+)"'
            matchs = re.findall(pattern, response.text)
            params = 'https://m.facebook.com/checkpoint' + str(matchs[0]).replace('&amp;', '&')
            pattern = r'name="fb_dtsg"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]
            pattern = r'name="jazoest"\s+value="(.*?)"'
            matchs = re.findall(pattern, response.text)
            jazoest = matchs[0]
            pattern = r'type="submit"\s+value="([^"]+)"\s+class="[^"]+"\s+name="action_upload_image"'
            matchs = re.findall(pattern, response.text)
            action_upload_image = matchs[0]

            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'origin': 'https://m.facebook.com',
                'referer': referer,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
            }


            # Get info facebook
            response_info_fb = self.get_info_fb(access_token_fb)
            response_info_fb = json.loads(response_info_fb)
            gen_face_100k = GenFace100K()
            response_gen_avatar = gen_face_100k.get_random_url_avatar()
            response_gen_avatar = json.loads(response_gen_avatar)
            if response_info_fb['status'] == 200:
                pass_port = passport()
                if response_gen_avatar['status'] == 200:
                    id_fb = response_info_fb['id']
                    # Up avatar
                    response_up_avatar = self.up_avatar(cookie, user_agent, id_fb)
                    response_up_avatar = json.loads(response_up_avatar)
                    if response_up_avatar['status'] == 200:
                        response = pass_port.save_url_image(id_fb, option_choise_Phoi + 1, response_gen_avatar['url'],
                                                            response_info_fb['first_name'],
                                                            response_info_fb['last_name'],
                                                            response_info_fb['birthday'], response_info_fb['gender'],
                                                            'HN')
                        response = json.loads(response)
                        if response['status'] == 200:
                            payload = {'fb_dtsg': fb_dtsg,
                                       'jazoest': jazoest,
                                       'action_upload_image': action_upload_image}
                            files = [
                                ('mobile_image_data',
                                 (f'{id_fb}.jpg',
                                  open(f'output_xmdt\{id_fb}.jpg', 'rb'), 'image/jpeg'))
                            ]
                            response = requests.request("POST", params, headers=headers, data=payload, files=files)
                            if response.text.__contains__('Review requested'):
                                return json.dumps({
                                    'status': 200,
                                    'message': 'XMDT thành công!',
                                })
                            else:
                                return json.dumps({
                                    'status': 200,
                                    'message': 'XMDT thất bại!',
                                })
                        else:
                            return json.dumps({
                                'status': 404,
                                'message': 'Lỗi tạo phôi'
                            })
                    else:
                        return json.dumps({
                            'status': 404,
                            'message': 'Lỗi up avatar!'
                        })
                else:
                    return json.dumps({
                        'status': 404,
                        'message': 'Lỗi tạo avatar'
                    })

            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Lỗi lấy thông tin facebook!'
                })

        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })

    def get_info_fb(self, access_token):
        try:
            url = "https://graph.facebook.com/v17.0/me?fields=id%2Cname%2Cfirst_name%2Clast_name%2Cbirthday%2Cgender&access_token=" + access_token

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            response = json.loads(response.text)
            gender = random.randrange(0, 2)
            if gender == 0:
                response['gender'] = 'male'
            else:
                response['gender'] = 'female'
            return json.dumps({
                'status': 200,
                'id': response['id'],
                'first_name': response['first_name'],
                'last_name': response['last_name'],
                'birthday': response['birthday'],
                'gender': response['gender'],
                'message': 'Lấy thông tin facebook thành công!',
            })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi lấy thông tin facebook!'
            })

    def up_avatar(self, cookie, user_agent, id_fb):
        try:
            response = self.make_request('https://www.facebook.com/profile.php?id=' + id_fb, 'GET',
                                         'www.facebook.com', 'https://www.facebook.com', False,
                                         '', user_agent, cookie, False, '')

            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
            pattern = r'"token":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            lsd = matchs[1]
            pattern = r'__a=(\d+)&__user=' + id_fb + '&__comet_req=(\d+)&jazoest=(\d+)'
            matchs = re.findall(pattern, response.text)
            a = matchs[0][0]
            comet_req = matchs[0][1]
            jazoest = matchs[0][2]
            pattern = r'"haste_session":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            haste_session = matchs[0]
            pattern = r'"connectionClass":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            ccg = matchs[0]
            pattern = r'"server_revision":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            rev = matchs[0]
            pattern = r'"hsi":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            hsi = matchs[0]
            pattern = r'"__spin_r":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            spin_r = matchs[0]
            pattern = r'"__spin_b":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            spin_b = matchs[0]
            pattern = r'"__spin_t":\s*(\d+)'
            matchs = re.findall(pattern, response.text)
            spin_t = matchs[0]
            pattern = r'"token":\s*"(.*?)"'
            matchs = re.findall(pattern, response.text)
            fb_dtsg = matchs[0]

            headers = {
                'authority': 'www.facebook.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/profile.php?id=' + id_fb,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent,
                'x-asbd-id': '129477',
                'x-fb-lsd': lsd,
                'accept-encoding': 'gzip, deflate, br',
                'connection': 'keep-alive',
            }

            params = {
                'profile_id': str(id_fb),
                'photo_source': '57',
                'av': str(id_fb),
                '__user': str(id_fb),
                '__a': str(a),
                '__req': 'v',
                '__hs': str(haste_session),
                'dpr': '1',
                '__ccg': str(ccg),
                '__rev': str(rev),
                '__s': '7srr4p:hs04x2:4qetvn',
                '__hsi': str(hsi),
                '__dyn': '7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyE24wJwpUe8hwaG0Z82_CxS320om78bbwto88422y11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2Sq2-azo2NwwwOg2cwMwhEkxe3u364UrwFg662S269wkopg6C',
                '__csr': 'gthAX34DaG7vtTqsCzigxlqN4RqOYyiSD4Oh6yky4t95jivRBjZOuqUyiBHJkQl4QExTBQaGHDjmnJ4iBhrgy-9GCq8AUyi48G_yapKqmFu8ADqWBCz9pFXGmKmXDCBzaCoyF9K8heeXDByAbGUy6UakfihS49ogy5UgGEnxyvUx3-4e8wgoLDgOim6Eyim48hgriwFxXyWCmUnyQ79p8f8C5p8ydxjxa9zVojUrxe2Gm3GeK224rUa85OfyA5U8U8o5XyUyiiq4E8E6-3e2iexq8xa01_owcXw0sGE04YS0ru2S0g2z02EE1kpU3Pw4tgbpUW4Ee82Dw8S1Tx63qEeo4q0w810o0aAj0dB03bo0rlwam2q2yeU0Aq5o1zEhwBgaeq2K0eVS0om03uF015K0HU0TSlwEyZHg3Lw61w4CwJVk4YM5p2o4V03rUhg1aE',
                '__comet_req': str(comet_req),
                'fb_dtsg': str(fb_dtsg),
                'jazoest': str(jazoest),
                'lsd': str(lsd),
                '__spin_r': str(spin_r),
                '__spin_b': str(spin_b),
                '__spin_t': str(spin_t),
            }

            payload = {}
            files = [
                ('file', (
                    f'{id_fb}.jpg', open(f'input_avatar\{id_fb}.jpg', 'rb'),
                    'image/jpeg'))
            ]

            response = requests.request('POST', 'https://www.facebook.com/profile/picture/upload/', params=params,
                                        headers=headers, data=payload, files=files, allow_redirects=True)
            response = json.loads(response.text.replace('for (;;);', ''))
            existing_photo_id = response['payload']['fbid']

            headers = {
                'authority': 'www.facebook.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/profile.php?id=' + id_fb,
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent,
                'x-asbd-id': '129477',
                'x-fb-friendly-name': 'ProfileCometProfilePictureSetMutation',
                'x-fb-lsd': lsd,
                'accept-encoding': 'gzip, deflate, br',
                'connection': 'keep-alive',
            }

            data = {
                'av': str(id_fb),
                '__user': str(id_fb),
                '__a': str(a),
                '__req': 'v',
                '__hs': str(haste_session),
                'dpr': '1',
                '__ccg': str(ccg),
                '__rev': str(rev),
                '__s': '7srr4p:hs04x2:4qetvn',
                '__hsi': '7247427489860976625',
                '__dyn': '7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyE24wJwpUe8hwaG0Z82_CxS320om78bbwto88422y11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2Sq2-azo2NwwwOg2cwMwhEkxe3u364UrwFg662S269wkopg6C',
                '__csr': 'gthAX34DaG7vtTqsCzigxlqN4RqOYyiSD4Oh6yky4t95jivRBjZOuqUyiBHJkQl4QExTBQaGHDjmnJ4iBhrgy-9GCq8AUyi48G_yapKqmFu8ADqWBCz9pFXGmKmXDCBzaCoyF9K8heeXDByAbGUy6UakfihS49ogy5UgGEnxyvUx3-4e8wgoLDgOim6Eyim48hgriwFxXyWCmUnyQ79p8f8C5p8ydxjxa9zVojUrxe2Gm3GeK224rUa85OfyA5U8U8o5XyUyiiq4E8E6-3e2iexq8xa01_owcXw0sGE04YS0ru2S0g2z02EE1kpU3Pw4tgbpUW4Ee82Dw8S1Tx63qEeo4q0w810o0aAj0dB03bo0rlwam2q2yeU0Aq5o1zEhwBgaeq2K0eVS0om03uF015K0HU0TSlwEyZHg3Lw61w4CwJVk4YM5p2o4V03rUhg1aE',
                '__comet_req': str(comet_req),
                'fb_dtsg': str(fb_dtsg),
                'jazoest': str(jazoest),
                'lsd': str(lsd),
                '__spin_r': str(spin_r),
                '__spin_b': str(spin_b),
                '__spin_t': str(spin_t),
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'ProfileCometProfilePictureSetMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1687423206551,708471,190055527696468,","caption":"","existing_photo_id":"' + existing_photo_id + '","expiration_time":null,"profile_id":"' + id_fb + '","profile_pic_method":"EXISTING","profile_pic_source":"TIMELINE","scaled_crop_rect":{"height":1,"width":1,"x":0,"y":0},"skip_cropping":true,"actor_id":"' + id_fb + '","client_mutation_id":"1"},"isPage":false,"isProfile":true,"sectionToken":"UNKNOWN","collectionToken":"UNKNOWN","scale":1}',
                'server_timestamps': 'true',
                'doc_id': '6421204037917926',
            }

            response = requests.request('POST', 'https://www.facebook.com/api/graphql/', headers=headers, data=data,
                                        allow_redirects=True)
            if response.text.__contains__(str(id_fb)):
                return json.dumps({
                    'status': 200,
                    'message': 'Up avatar thành công'
                })
            else:
                return json.dumps({
                    'status': 404,
                    'message': 'Lỗi up avatar!'
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi server!'
            })
