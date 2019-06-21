
.. include:: links.inc

To use lxd_module
#################
require::

    sudo apt-get install python-pylxd lxd


delete object except container::

    sudo python3 utils2devops/lxd_lxc/lxc_delete.py

    usage: lxc_delete.py [-h] [-v] [-e ENDPOINT] [-c CERT] [-sure SURE]
                         [-deleteAllImages] [-deleteAllNetworks]
                         [-deleteAllProfiles] [-deleteAllStorages]

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -deleteAllImages      DELETE all lxc image
      -deleteAllNetworks    DELETE all lxc network
      -deleteAllProfiles    DELETE all lxc profile
      -deleteAllStorages    DELETE all lxc storage

      -e ENDPOINT, --endpoint ENDPOINT
                            the endpoint if not local
      -c CERT, --cert CERT  tuple of (cert, key) like ('/path/to/client.crt',
                            '/path/to/client.key')
      -sure SURE            Required for all deleteAll* with value YES_I_AM_SURE


container management::

    sudo python3 utils2devops/lxd_lxc/lxc_container.py

    usage: lxc_container.py [-h] [-v] [-e ENDPOINT] [-c CERT] [-sure SURE]
                            (-statusAll | -deleteAll | -startAll | -stopAll)
                            [-controller_uuid CONTROLLER_UUID]
                            [-model_uuid MODEL_UUID]
    lxc_container.py: error: one of the arguments -statusAll -deleteAll -startAll -stopAll is required

TODO the documentation of existing functionnalities
TODO implementation WORK IN PROGESS
