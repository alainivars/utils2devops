#!/home/alain/venv/utils2devops/bin/python
import argparse

from utils2devops.lxd import __version__
from utils2devops.lxd.container import Container

parser = argparse.ArgumentParser()
parser.add_argument('-V', '--version', action='version', version=__version__)
group1 = parser.add_argument_group()
group1.add_argument('-v', '--verbose', type=int, default=0,
                    help='verbose infos: 0=none, 1=Little, 2=more, 3=full')
group1.add_argument('-e', '--endpoint', help='the endpoint if not local')
group1.add_argument('-c', '--cert', help='''
tuple of (cert, key) like ('/path/to/client.crt', '/path/to/client.key')''')
group1.add_argument('-sure', default='NO_I_AM_NOT_SURE', help='''
    Required for deleteAll with value YES_I_AM_SURE''')
group2 = parser.add_mutually_exclusive_group(required=True)
group2.add_argument('-statusAll', action='store_true', default=False,
                    help='give the status of all container')
group2.add_argument('-deleteAll', action='store_true', default=False,
                    help='delete all container')
group2.add_argument('-startAll', action='store_true', default=False,
                    help='start all container')
group2.add_argument('-stopAll', action='store_true', default=False,
                    help='stop all container')
group3 = parser.add_argument_group()
group3.add_argument('-controller_uuid', default='', required=False, help='''
    All container of that controller UUID, get it with -d -statusAll''')
group3.add_argument('-model_uuid', default='', required=False, help='''
    All container of that model UUID, get it with -d -statusAll''')


if __name__ == '__main__':
    args = parser.parse_args()
    if args.endpoint:
        object = Container(args.verbose, args.endpoint, args.cert)
    else:
        object = Container(args.verbose)
    if args.statusAll:
        object.status_all()
    elif args.startAll:
        object.start_all(args.controller_uuid, args.model_uuid)
    elif args.stopAll:
        object.stop_all(args.controller_uuid, args.model_uuid)
    elif args.deleteAll and args.sure == 'YES_I_AM_SURE':
        object.delete_all(args.controller_uuid, args.model_uuid)
    else:
        print(parser.format_help())
