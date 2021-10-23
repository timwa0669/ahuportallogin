import requests
from urllib.parse import *
import random
import dns.resolver

random.seed(a=None, version=2)


def gen_random_num():
    return random.randint(500, 10500)


class Portal:
    captive_portal_address = '223.5.5.5'
    login_url = 'http://172.16.253.3:801/eportal/'
    logout_url_wired = 'http://172.16.253.3:801/eportal/?c=Portal&a=logout&callback=dr1004&login_method=1&ac_logout=0&register_mode=1'
    logout_domain_wireless = 'securelogin.arubanetworks.com'
    dns_server = '172.16.252.3'

    portal_request_result = None
    login_params = {}
    login_params_queried = {}

    def __init__(self):
        if not self.is_logged_in():
            self.get_login_params()
            self.set_login_params()

    def get_captive_portal_url(self, captive_portal_address):
        return 'http://' + captive_portal_address + '/?cmd=redirect&arubalp=12345'

    def get_logout_url_wireless(self, url):
        return 'http://' + url + '/auth/logout.html'

    def set_credentials(self, usr, pwd):
        self.login_params['user_account'] = usr
        self.login_params['user_password'] = pwd

    def set_login_params(self):
        self.login_params['c'] = 'Portal'
        self.login_params['a'] = 'login'
        self.login_params['callback'] = 'dr1003'
        self.login_params['wlan_user_ipv6'] = ''
        self.login_params['wlan_ac_name'] = ''
        self.login_params['jsVersion'] = '3.3.2'
        if self.login_params['login_method'] == 1:
            self.login_params['wlan_user_ip'] = self.login_params_queried['wlanuserip']
            self.login_params['wlan_user_mac'] = '000000000000'
            self.login_params['wlan_ac_ip'] = self.login_params_queried['wlanacip']
        elif self.login_params['login_method'] == 8:
            self.login_params['wlan_user_ip'] = self.login_params_queried['ip']
            self.login_params['wlan_user_mac'] = self.login_params_queried['mac'].replace(':', '')
            self.login_params['wlan_ac_ip'] = self.login_params_queried['switchip']
        self.login_params['v'] = gen_random_num()

    def get_login_params(self):
        self.login_params_queried = dict(parse_qsl(self.portal_request_result.query))
        if 'essid' in self.login_params_queried:
            self.login_params['login_method'] = 8
        else:
            self.login_params['login_method'] = 1

    def is_logged_in(self):
        r = requests.get(self.get_captive_portal_url(self.captive_portal_address))
        self.portal_request_result = urlsplit(r.url)
        if self.portal_request_result.netloc == self.captive_portal_address:
            return True
        else:
            return False

    def request_login(self):
        r = requests.get(self.login_url, params=self.login_params)

    def request_logout(self):
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [self.dns_server]
        resolver.timeout = 1.5
        try:
            answers = resolver.resolve(self.logout_domain_wireless, 'A')
        except dns.resolver.NoNameservers:
            r = requests.get(self.logout_url_wired)
        except dns.exception.Timeout:
            r = requests.get(self.logout_url_wired)
        else:
            for i in answers:
                r = requests.get(self.get_logout_url_wireless(str(i)))
