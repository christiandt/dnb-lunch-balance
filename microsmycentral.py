import urllib
import requests
import re


class MicrosMycentral:

    def __init__(self):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.Session()
        self.initiate_session()

    def initiate_session(self):
        headers = {'Connection': 'keep-alive'}
        headers['Upgrade-Insecure-Requests'] = "1"
        headers['Sec-Fetch-Mode'] = "navigate"
        headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
        headers['Sec-Fetch-Site'] = "none"
        headers['Accept-Encoding'] = "gzip, deflate, br"
        headers['Accept-Language'] = "en-US,en;q=0.9,da;q=0.8,nb;q=0.7"

        url = "https://dnb.microsmycentral.com/"

        response = self.session.get(url=url, headers=headers, verify=False)
        return response.status_code == 200

    def post_credentials(self, username, password):
        username_encoded = urllib.quote(username)
        headers = {'Connection': 'keep-alive'}
        headers['Cache-Control'] = "max-age=0"
        headers['Origin'] = "https://dnb.microsmycentral.com"
        headers['Upgrade-Insecure-Requests'] = "1"
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        headers['Sec-Fetch-Mode'] = "navigate"
        headers['Sec-Fetch-User'] = "?1"
        headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
        headers['Sec-Fetch-Site'] = "same-origin"
        headers['Referer'] = "https://dnb.microsmycentral.com/Pages/Account/Login/Default.aspx"
        headers['Accept-Encoding'] = "gzip, deflate, br"
        headers['Accept-Language'] = "en-US,en;q=0.9,da;q=0.8,nb;q=0.7"
        data="__EVENTTARGET=ctl00%24MainContent%24ucLoginStatusContainer%24MiniLoginRegister1%24ucLogin%24LoginLinkButton%24lnkLinkButton&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTM4NDExNjE3NQ9kFgJmD2QWBAIBD2QWAgIDDxUFLS9Db21tb24vUmVzb3VyY2VzL1NjcmlwdHMvanF1ZXJ5LTEuNi4yLm1pbi5qczgvQ29tbW9uL1Jlc291cmNlcy9TY3JpcHRzL2pxdWVyeS11aS0xLjguMTYuY3VzdG9tLm1pbi5qcywvQ29tbW9uL1Jlc291cmNlcy9TY3JpcHRzL2pxdWVyeS50bXBsLm1pbi5qcygvQ29tbW9uL1Jlc291cmNlcy9TY3JpcHRzL0NoZWNrTnVtYmVyLmpzIi9Db21tb24vUmVzb3VyY2VzL1NjcmlwdHMvanNvbjIuanNkAgMPZBYCAgEPZBYIAgEPZBYCAgEPZBYCAgEPZBYCZg9kFgICAQ8WAh4EaHJlZgUNfi9uYi1OTy9Ib21lL2QCAw9kFgICAQ9kFgICAQ9kFgJmDzwrAAoBAA8WAh4IVXNlck5hbWVkZBYCZg9kFgICAQ9kFgQCEw8PZBYCHgVzdHlsZQUNZGlzcGxheTpub25lO2QCFQ8PFgIeC05hdmlnYXRlVXJsBVt%2BL25iLU5PL015QWNjb3VudC9QYXNzd29yZC9EZWZhdWx0LmFzcHg%2FUmV0dXJuVXJsPSUyZlBhZ2VzJTJmQWNjb3VudCUyZkxvZ2luJTJmRGVmYXVsdC5hc3B4ZGQCBA9kFgICAQ9kFgJmD2QWAgIDD2QWAmYPEA8WCB4NRGF0YVRleHRGaWVsZAULQ3VsdHVyZVRleHQeDkRhdGFWYWx1ZUZpZWxkBQtDdWx0dXJlQ29kZR4LXyFEYXRhQm91bmRnHgdWaXNpYmxlaGQQFQEbTm9yd2VnaWFuLCBCb2ttw6VsIChOb3J3YXkpFQEFbmItTk8UKwMBZxYBZmQCBg9kFgQCAQ8PFgIeBFRleHQFDm1uOiBGUk1OV0VCMDc7ZGQCAw8PFgIfCAULdjogNC4wLjAuMDtkZGR1xU1EsVeJKuYleUr3EG0eJxMJJQ%3D%3D&__VIEWSTATEGENERATOR=E15A7D43&__SCROLLPOSITIONX=0&__SCROLLPOSITIONY=0&__EVENTVALIDATION=%2FwEdAAb0IZjYMFBPFJ71enOD042uodAjP11z%2BqSWlRW31c5Vg0fY2gOgiEZW9HlhUvRq6zF4EVnfB9j0%2FN4LGCkRHvC05WpMzsEeaY6MZOc3jaUCsbYytuZ9xbV0d4kpyUuDp%2FY%2BqqSb%2FPEZazhQ5xPZQdyPZeO7Ag%3D%3D&ctl00%24MainContent%24ucLoginStatusContainer%24MiniLoginRegister1%24ucLogin%24UserName={}&ctl00%24MainContent%24ucLoginStatusContainer%24MiniLoginRegister1%24ucLogin%24Password={}".format(username_encoded, password)

        url = "https://dnb.microsmycentral.com/Pages/Account/Login/Default.aspx"

        response = self.session.post(url=url, headers=headers, data=data, verify=False)
        return response.status_code == 200

    def get_current_balance(self):
        headers = {'Connection': 'keep-alive'}
        headers['Upgrade-Insecure-Requests'] = "1"
        headers['Sec-Fetch-Mode'] = "navigate"
        headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
        headers['Sec-Fetch-Site'] = "none"
        headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        headers['Accept-Encoding'] = "gzip, deflate, br"
        headers['Accept-Language'] = "en-US,en;q=0.9,da;q=0.8,nb;q=0.7"

        url = "https://dnb.microsmycentral.com/"

        response = self.session.get(url=url, headers=headers, verify=False)
        try:
            m = re.search(': kr (.+?)</span>', response.text)
            return float(m.group(1).replace(',', '.'))
        except AttributeError:
            raise Exception("Unable to fetch balance, check credentials")
