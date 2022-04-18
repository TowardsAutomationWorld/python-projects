import json

settings = None


class GlobalConfig:

    @staticmethod
    def readConfigValues(jsonKey):
        with open('D:\\PythonPracticeWorkspace\\BDDCucumber\\resources\\config\\GlobalSettings.json', 'r') as jsonfile:
            settings = json.load(jsonfile)
            return settings[jsonKey]
