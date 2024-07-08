import os


HOME_DIR = os.path.expanduser("~")


class Config:

    DATA_ROOT = os.path.join(HOME_DIR, "data")
    OPT_ROOT = os.path.join(HOME_DIR, "opt")
