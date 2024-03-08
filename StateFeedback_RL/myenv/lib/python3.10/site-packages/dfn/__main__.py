import argparse as arg
import os

from .util import download_from_nas

def dfn_parser():
    parser = arg.ArgumentParser(description     = "download_drom_nas",
                                formatter_class = arg.ArgumentDefaultsHelpFormatter,
                                prog            = "python -m dfn")
    required_group = parser.add_argument_group("required", "required parameters for compilation")
    required_group.add_argument("--url",
                                type    = str,
                                help    = "url")
    return parser
if __name__ == "__main__":
    parser = dfn_parser()
    a = parser.parse_args()
    download_from_nas(a.url)
    