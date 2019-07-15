import configparser


def getConfig(file):
    config = configparser.ConfigParser()
    config.sections()
    config.read(file)
    return config
