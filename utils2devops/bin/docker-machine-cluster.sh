#!/bin/bash
#set -x

#
# Just a quick script to create and destroy a local docker-machine-cluster
#

count=0
actions=()

usage()
{
    echo "usage:"
    echo "  docker-machine-cluster [-h | --help] To get this help"
    echo "  docker-machine-cluster [-c | --create x]"
    echo "      Where x is the number of manager node to create/add in the swarm."
    echo "  docker-machine-cluster [-d | --destroy x]"
    echo "      Where x is the number of manager node to create/add in the swarm."
}


if [ -z $1 ];then
    actions=(usage)
fi

while [ "$1" != "" ]; do
    case $1 in
        -c | --create )
            shift
            if [ -z "$1" ]
            then
                echo "You must give a number of node to create"
                exit 1
            else
                count=$1
            fi
            actions=(create_nodes)
            ;;
        -d | --destroy )
            shift
            actions=(destroy_nodes)
            if [ -z "$1" ]
            then
                echo "You must give a number of node to destroy"
                exit 1
            else
                count=$1
            fi
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
let nodes=manager_count+worker_count

if [ -z "${DOCKER_MACHINE_DRIVER}" ]; then
    DOCKER_MACHINE_DRIVER=virtualbox
fi

MACHINE_OPTS="--engine-storage-driver overlay2"

function create_nodes() {
    for i in $(seq 1 ${count})
    do
        echo "Create node-${i}"
        docker-machine create -d ${DOCKER_MACHINE_DRIVER} ${MACHINE_OPTS} node-${i}
    done
}

function destroy_nodes() {
    for i in $(seq 1 ${count})
    do
        echo "Destroy node-${i}"
        docker-machine rm -y node-${i}
    done
}

for action in "${actions[@]}"
do
    ${action}
    sleep 1
done
echo "Job done..."
echo -ne '\007'
