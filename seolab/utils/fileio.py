import os


def make_parent_dir(path):
    parent_dir = os.path.dirname(os.path.abspath(os.path.normpath(path)))
    os.makedirs(parent_dir, exist_ok=True)
