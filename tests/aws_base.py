from weakref import WeakValueDictionary


class Singleton(type):
    """
    Author: Ashwini Chaudhary (https://stackoverflow.com/users/846892/ashwini-chaudhary)
    Description: Instead of defining a custom method for deleting the instance reference
    use a WeakValueDictionary. Now when there are no more references of MockObject anywhere
    it will be cleaned up from Singleton._instances automatically.
    """
    _instances = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # This variable declaration is required to force a
            # strong reference on the instance.
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClientExceptionServiceName(Exception):
    pass


class SingletonClientExceptionRegionName(Exception):
    pass


class SingletonClient(metaclass=Singleton):
    """
    Singleton Client, maybe that is a wrong way and we will need more to one
    but we will see, but it's for unit test and that should be enough.
    """

    def __init__(self, service_name: str, region_name: str):
        """
        Overwrite the new operator to return always the same instance,
        if the instance already exist we don't modify it, we just
        return it.

        :param service_name: a string with the name of service in AWS
        :param region_name: The AWS region to use.
        :return:
        """
        if service_name not in ['ec2', 'lambda', 's3']:
            message = 'the service name is not implemented or do not exist'
            self.error = message
            raise SingletonClientExceptionServiceName(message)
        self.service_name = service_name
        if region_name not in ['us-east-1', 'us-east-2']:
            message = 'the region name is not implemented or do not exist'
            self.error = message
            raise SingletonClientExceptionRegionName(message)
        self.region_name = region_name
        self.lambda_functions = {}
        self.lambda_conf = {}
        self.network_acls_elements = []
        self.s3_bucket_data = []
        self.error = None

    def describe_network_acls(self):
        if self.service_name == 'ec2':
            return self.network_acls_elements
        else:
            return []

    @staticmethod
    def get_public_access_block(bucket):
        return {'PublicAccessBlockConfiguration': {'BlockPublicAcls': 'private'}}

    def list_buckets(self):
        if self.service_name == 's3':
            return self.s3_bucket_data
        return []

    def list_functions(self):
        if self.service_name == 'lambda':
            return self.lambda_functions
        return []

    def get_function(self, function_name):
        if self.service_name == 'lambda':
            return self.lambda_conf
        return []


class SingletonResourceExceptionServiceName(Exception):
    pass


class SingletonResourceExceptionRegionName(Exception):
    pass


class SingletonResource(metaclass=Singleton):
    """
    Singleton Resource, maybe that is a wrong way and we will need more to one
    but we will see, but it's for unit test and that should be enough.
    """

    class _Conf:
        status = 'Disabled'

    def __init__(self, service_name: str, region_name: str):
        """
        Overwrite the new operator to return always the same instance,
        if the instance already exist we don't modify it, we just
        return it.

        :param service_name: a string with the name of service in AWS
        :param region_name: The AWS region to use.
        :return:
        """
        if service_name not in ['lambda', 's3']:
            message = 'the service name is not implemented or do not exist'
            self.error = message
            raise SingletonResourceExceptionServiceName(message)
        self.service_name = service_name
        if region_name not in ['us-east-1', 'us-east-2']:
            message = 'the region name is not implemented or do not exist'
            self.error = message
            raise SingletonResourceExceptionRegionName(message)
        self.region_name = region_name
        self.profile_exist = True
        self.conf = SingletonResource._Conf

    def bucket_versioning(self, bucket_name):
        return self.conf


class SingletonSession(metaclass=Singleton):
    """
    Singleton Session, maybe that is a wrong way and we will need more to one
    but we will see, but it's for unit test and that should be enough.
    """

    def __init__(self, profile_name: str):
        """
        Overwrite the new operator to return always the same instance,
        if the instance already exist we don't modify it, we just
        return it.

        :param profile_name: The AWS profile name to use.
        :return:
        """
        self.profile_name = profile_name
        self.profile_exist = True
        self.singletonClient = None

    def client(self, service_name: str, region_name: str):
        # self.service_name = service_name
        # self.region_name = region_name
        self.singletonClient = SingletonClient(service_name, region_name)
        return self.singletonClient


if __name__ == '__main__':
    m = SingletonSession(profile_name='test1')
    n = SingletonSession(profile_name='test2')
    print(dict(Singleton._instances))
    del m
    print(dict(Singleton._instances))
    del n
    print(dict(Singleton._instances))
    try:
        SingletonClient(service_name='monopole', region_name='us-east-1')
    except SingletonClientExceptionServiceName as e:
        pass
    try:
        SingletonClient(service_name='ec2', region_name='the-moon')
    except SingletonClientExceptionRegionName as e:
        pass
