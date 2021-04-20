#!/bin/bash
#set -x

#
# Just a quick script to create and destroy a local docker-machine-cluster
#
# Docker-machine (DEPRECATED)

count=0
actions=()
mask="node-"

usage()
{
    echo "usage:"
    echo "  docker-machine-cluster [-h | --help] To get this help"
    echo "  docker-machine-cluster [-c | --create x] [-m | --mask y]"
    echo "      Where x is the number of node to create/add."
    echo "      Where y is the mask of the node: example: node. or server-, default is node-"
    echo "  docker-machine-cluster [-d | --destroy x] [-m | --mask y]"
    echo "      Where x is the number of node to destroy."
    echo "      Where y is the mask of the node: example: node. or server., default is node."
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
        -m | --mask )
            shift
            if [ -z "$1" ]
            then
                mask="node."
            else
                mask=$1
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

# Docker-machine (DEPRECATED)
if [ -z "${DOCKER_MACHINE_DRIVER}" ]; then
  DOCKER_MACHINE_DRIVER=virtualbox
fi
#if [ -z "${DOCKER_MACHINE_OS}" ]; then
#  # Boot2Docker (DEPRECATED)
#  #  DOCKER_MACHINE_OS="/media/a/disk4/ISOs/photon-minimal-4.0.iso"
#  DOCKER_MACHINE_OS="https://releases.rancher.com/os/latest/rancheros.iso"
#fi

MACHINE_OPTS="--engine-storage-driver overlay2"

function create_nodes() {
    for i in $(seq 1 ${count})
    do
        echo "Create ${mask}${i}"
#        docker-machine create -d ${DOCKER_MACHINE_DRIVER} \
#          --virtualbox-boot2docker-url ${DOCKER_MACHINE_OS} \
#          ${MACHINE_OPTS} ${mask}${i}
        docker-machine create -d ${DOCKER_MACHINE_DRIVER} ${MACHINE_OPTS} ${mask}${i}
    done
}

function destroy_nodes() {
    for i in $(seq 1 ${count})
    do
        echo "Destroy ${mask}${i}"
        docker-machine rm -y ${mask}${i}
    done
}

for action in "${actions[@]}"
do
    ${action}
    sleep 1
done
echo "Job done..."
echo -ne '\007'
