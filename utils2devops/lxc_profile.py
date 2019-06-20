#!/home/alain/venv/utils2devops/bin/python
import argparse

from utils2devops.lxd import __version__
from utils2devops.lxd.profile import Profile


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version=__version__)
    group1 = parser.add_argument_group()
    group1.add_argument('-e', '--endpoint', help='the endpoint if not local')
    group1.add_argument('-c', '--cert', help='''
    tuple of (cert, key) like ('/path/to/client.crt', '/path/to/client.key')''')
    group1.add_argument('-sure', default='NO_I_AM_NOT_SURE', help='''
    Required for deleteAll with value YES_I_AM_SURE''')
    parser.add_argument('-deleteAll', action='store_true', default=False, required=False,
                        help='give the status of all lxc profile')

    args = parser.parse_args()
    if args.endpoint:
        object = Profile(args.endpoint, args.cert)
    else:
        object = Profile()
    if args.deleteAll and args.sure == 'YES_I_AM_SURE':
        object.delete_all()
    else:
        print(parser.format_help())
