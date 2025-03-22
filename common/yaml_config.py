# with open('../config/enviroment.yaml', "r", encoding= "utf-8") as f:
#     r = f.read()
#     print(r)

# 使用pyyaml读取
import yaml
from common.tools import get_project_path, file_sep
class GetConf:
    def __init__(self):
        enviroment_yaml_path = get_project_path() + file_sep(["config", "enviroment.yaml"], add_sep_before=True)
        with open(enviroment_yaml_path, "r", encoding= "utf-8") as f:
            self.env = yaml.load(f, Loader=yaml.FullLoader)
            # print(self.env)

    def get_user_pass(self, user):
        # return self.env["username"], self.env["password"]
        return self.env["user"][user]['username'], self.env["user"][user]['password']

    def get_url(self):
        return self.env["URL"]

if __name__ == '__main__':
    # GetConf()
    conf = GetConf()
    print(conf.get_user_pass())
    print(conf.get_url())