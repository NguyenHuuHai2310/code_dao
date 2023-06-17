import json
import re
from urllib.parse import urlencode, quote

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
            else:
                previous_cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in response.history[0].cookies])
                if str(previous_cookie).__contains__('checkpoint=deleted'):
                    cookies = cookies + str(previous_cookie).replace('checkpoint=deleted', '')
                else:
                    cookies = cookies + '; ' + previous_cookie
                return json.dumps({
                    'status': 200,
                    'cookie': cookies,
                    'message': 'Đăng nhập thành công!',
                })
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
