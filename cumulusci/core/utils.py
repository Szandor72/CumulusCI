""" Utilities for CumulusCI Core

import_class: Task class defn import helper """

import logging
import os
import sys


def import_class(path):
    """ Import a class from a string module class path """
    components = path.split('.')
    module = components[:-1]
    module = '.'.join(module)
    sys.path.append(os.getcwd())
    mod = __import__(module, fromlist=[components[-1]])
    return getattr(mod, components[-1])
