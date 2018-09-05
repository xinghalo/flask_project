import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    A = 1
    B = 2
    name = "basic"

class DevConfig(Config):
    name = "dev"

class TestConfig(Config):
    name = "test"

class PreConfig(Config):
    name = "pre"

class OnlineConfig(Config):
    name = "online"

config = {
    'dev' : DevConfig,
    'test': TestConfig,
    'pre' : PreConfig,
    'online':OnlineConfig,

    'default': DevConfig
}