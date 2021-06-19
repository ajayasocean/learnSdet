# configurations here
import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('config/globalProperties.ini')
    return config
