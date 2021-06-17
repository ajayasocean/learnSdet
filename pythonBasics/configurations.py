# configurations here
import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('globalProperties.ini')
    return config
