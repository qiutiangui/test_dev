import yaml
from string import Template
from jmespath import search
import os

from common.data_common import login


class ReadYaml(object):
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as fp:
            read_yaml_str = fp.read()
            template = Template(read_yaml_str)
            c = template.safe_substitute({"token": login()})

        dict_data = yaml.safe_load(c)
        return dict_data


if __name__ == '__main__':
    datapath = os.path.join(os.path.abspath('..'), "data")
    filepath = os.path.join(datapath, "query.yml")
    data = ReadYaml(filepath)
    response = data.read_yaml()
    print(response)
