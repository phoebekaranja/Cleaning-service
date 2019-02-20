# import os
class Config():
    pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
config_options = {
        'production':ProdConfig,
        'development':DevConfig,
        'test':TestConfig
     }

class TestConfig(Config):
    pass
