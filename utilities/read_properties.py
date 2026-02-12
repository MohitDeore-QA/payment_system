import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    @staticmethod
    def get_project_url():
        url= config.get('project login info','project_url')
        return url
    @staticmethod
    def get_username():
        username= config.get('project login info','username')
        return username
    @staticmethod
    def get_password():
        password = config.get('project login info','password')
        return password
    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('project login info','invalid_username')
        return invalid_username
