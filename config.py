class Config:
    def __init__(self, env):

        self.base_url = {
            'dev': 'https://miratelier.com',
            'qa': 'https://qa.miratelier.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]
