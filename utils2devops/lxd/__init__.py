from pylxd import Client

__version__='0.1.0'


class BaseLXD:
    """ missing feature for command line """
    def __init__(self, debug=False, endpoint=None, cert=None):
        """
        :param endpoint: str like "https://192.83.9.23:8367"
        :param cert: tuple of (cert, key) like
                    ('/path/to/client.crt', '/path/to/client.key')
        """
        self.DEBUG = debug
        self.client = Client(endpoint=endpoint, cert=cert)

