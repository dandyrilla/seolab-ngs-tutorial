import os

import pandas as pd


def make_parent_dir(path):
    parent_dir = os.path.dirname(os.path.abspath(os.path.normpath(path)))
    os.makedirs(parent_dir, exist_ok=True)


def read_tsv(filename, **kw):
    _kw = dict(sep='\t', header=0)
    _kw.update(kw)
    df = pd.read_csv(filename, **_kw)
    return df


def to_tsv(df, filename, **kw):
    make_parent_dir(filename)
    _kw = dict(sep='\t', index=False)
    _kw.update(kw)
    df.to_csv(filename, **_kw)
