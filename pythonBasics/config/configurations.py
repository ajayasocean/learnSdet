# configurations here
import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('config/globalProperties.ini')
    return config
