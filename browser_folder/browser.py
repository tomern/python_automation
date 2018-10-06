from selenium import webdriver
from browser_folder.browser_helper import BrowserHelper


class Browser:
    def __init__(self, cfg, request):
        self.driver = webdriver.Chrome(executable_path=cfg.chrome_path) if cfg.local \
            else webdriver.Remote('http://{0}:{1}/wd/hub'.format(cfg.my_ip, cfg.sel_port), self.get_cap(cfg, request))
        self.browser_helper = BrowserHelper(self.driver)
        self.maximize_window()

    def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def get_url(self):
        return self.driver.current_url

    def maximize(self):
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_cap(self, cfg, request):
        desired_caps = dict()
        desired_caps['browserName'] = cfg.browser_type
        desired_caps['enableVNC'] = cfg.selenoid_caps['enable_vnc']
        desired_caps['enableVideo'] = cfg.selenoid_caps['enable_video']
        desired_caps['name'] = request.node.name
        return desired_caps

    def maximize_window(self):
        try:
            self.driver.maximize_window()
        except:
            pass
