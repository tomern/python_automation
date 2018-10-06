
class Config:
    def __init__(self, env):
        self.local = True
        self.env = env
        self.my_ip = '10.100.102.7'
        self.rerun = 1
        self.sel_port = '4444'
        self.chrome_path = r'C:\Users\tomern23\Desktop\chromedriver.exe'
        self.browser_type = 'chrome'
        self.number = 1
        self.image = 'C:/Users/tomern23/Pictures/Cat.jpg'
        self.selenoid_caps = {
            'enable_vnc': True,
            'enable_video': True
        }
        self.urls = {
            'google_url': 'http:\\www.google.com',
            'walla_url': 'http:\\www.walla.com',
            'jamesallen_url': 'https://www.jamesallen.com',
            'service_url': 'https://httpbin.org'
        }
        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com'
        }[env]
        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]
        self.cloudinary = {
            'cloud_name': 'doomw8apy',
            'api_key': "455829723853644",
            'api_secret': "bAw3EPy5A85ZE693hjAHGj8I7kM"
        }
        self.user_jamesallen = {
            'username': 'tomernoy1@gmail.com',
            'password': '123456'
        }



