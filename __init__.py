import os
from cudatext import *
from . import format_proc
from . import yaml

format_proc.MSG = '[YAML Format] '

def do_format(text):

    obj = yaml.load(text)
    return yaml.dump(obj)

class Command:

    def run(self):

        format_proc.run(do_format)
