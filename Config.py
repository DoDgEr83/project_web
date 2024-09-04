import json


class Config:
    def __init__(self):
        with open('config.json') as file:
            self.data = json.load(file)

    def __call__(self, parm):
        return self.data.get(parm)

config = Config()


# if __name__ == "__main__":
#     print(config.data.get('conn_str'))
#     print(config('conn_str'))