#!/bin/bash
#set -x

#
# TODO: delete if useless
# Inspired by: https://github.com/BretFisher/dogvscat
# Just a quick script to a local swarm enable-monitoring
#

count=0
path=""
actions=()

usage()
{
    echo "usage:"
    echo "  enable-monitoring [-h | --help] To get this help"
    echo "  enable-monitoring [-p path -n | --number x]"
# TODO    echo "  enable-monitoring [-n | --number x [-t | --template node-]]"
    echo "      Where x is the number of node to add enable the monitoring in the swarm."
    echo "      Where path is the path of the daemon.json."
}


if [ -z $1 ];then
    actions=(usage)
fi

while [ "$1" != "" ]; do
    case $1 in
        -p | --path )
            shift
            if [ -z "$1" ]
            then
                echo "You must give the path of the daemon.json"
                exit 1
            else
                if [ -e $1 ]
                then
                    path=$1
                else
                    echo "ERROR: the file "${1}daemon.json" don not exit!!!"
                    exit 1
                fi
            fi
            actions=(enable_monitoring)
            ;;
        -n | --number )
            shift
            if [ -z "$1" ]
            then
                echo "You must give a number of node to enable the monitoring"
                exit 1
            else
                count=$1
            fi
            actions=(enable_monitoring)
            ;;
        -h | --help )
            actions=(usage)
            exit
            ;;
        * )
            actions=(usage)
            exit 1
    esac
    shift
done

echo "started..."

function enable_monitoring() {
    for i in $(seq 1 ${count})
    do
        echo "Enable the monitoring on node-${i}"
#          docker-machine scp ${path}daemon.json node-${i}:/etc/docker
# workaround because https://github.com/docker/machine/issues/2722
          docker-machine scp ${path}daemon.json node-${i}:/tmp
          docker-machine ssh node-${i} sudo cp /tmp/daemon.json /etc/docker
#          docker-machine ssh node-${i} systemctl restart docker &
# workaround because it a boot2docker image and systemctl is not present
          docker-machine restart node-${i}
    done
}

for action in "${actions[@]}"
do
    ${action}
    sleep 1
done
echo "Job done..."
echo -ne '\007'
